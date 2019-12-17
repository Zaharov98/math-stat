install.packages(c("RCurl", "rjson", "igraph"))

library(RCurl)
library(rjson)
library(igraph)

access_token <- "access_token" # put your token there
api_version <- "5.45"

vk <- function(method, params) {
  if (!missing(params)) {
    params <- sprintf("?%s", paste(names(params), "=",
                                   unlist(params), collapse = "&", sep = ""))
  } else {
    params <- ""
  }
  
  url <- sprintf("https://api.vk.com/method/%s%s&access_token=%s&v=%s",
                 method, params, access_token, api_version)
  data <- getURL(url)
  
  tryCatch({
    list <- fromJSON(data)
  }, error = function(e) {
    print(data)
    stop(e)
  })
  
  list$response
}

uid <- "uid" # put your uid here
friendList <- vk("friends.get", list(user_id = uid))

count <- friendList$count
ids <- friendList$items

friendLists <- vector(length = count)
for (i in 1:count) {
  params <- list(user_id = ids[i])
  list <- vk("friends.get", params)
  friendLists[i] <- list(list$items)
}
friendLists <- c(friendLists, list(ids))

n <- length(friendLists)
mutuals <- matrix(nrow = n, ncol = n)
for (i in 1:n) {
  for (j in 1:n) {
    mutuals[i,j] <- sum(friendLists[[i]] %in% friendLists[[j]])
  }
}

g <- graph_from_adjacency_matrix(mutuals, weighted = T, mode = "undirected", diag = F)
V(g)$name <- as.character(1:n)

isolated <- V(g)[degree(g) == 0]
g <- g - vertices(isolated)

egam <- max(E(g)$weight + .5) / (E(g)$weight + .5)
coord <- layout_with_kk(g, weights = egam)

png(file = "graph.png")
plot(g, layout = coord, vertex.size = 15)
dev.off()
