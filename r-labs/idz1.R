# Boston housing 

# Uncomment this statement to restore dependencies
# install.packages("NbClust")
# install.packages("ggplot2")

library(NbClust)
library(MASS)
library(ggplot2)

# import data set
boston = Boston
head(boston)

#================================================================
# Hierarchical clusterisation
#================================================================
# normilaze data set
normalized <- scale(boston[, 0:14], center = T, scale = T)
dist <- dist(normalized[, 0:14])
head(normalized)

# implement hierarchical clustering
clust <- hclust(dist, method = "ward.D")

list(clust)
plot(clust, labels = clust$medv, cex=.7)
# rect.hclust(clust, k=4, border = "red")

# factor scree
nclust <- seq(length(clust$height), 1, -1)
plot(nclust, clust$height, type = "b",
        xlab = "Number of clusters",
        ylab = "Height",
        main = "Scree plot")

#================================================================
# K-mean
#================================================================
# perform k-means clustering on a data matrix
clust <- kmeans(normalized[, 0:14], centers = 3, nstart = 20)
clust

clust$cluster <- as.factor(clust$cluster)
ggplot(boston, aes(x = boston$medv, y = boston$dis, color = clust$cluster)) + geom_point()
