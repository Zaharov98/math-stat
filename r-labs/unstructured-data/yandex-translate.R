library(RSelenium)

rD <- rsDriver(remoteServerAddr = "localhost",
                   port = 8895L,
                   browser = "firefox")
rd <- rD[["client"]]
rd$open()
rd$navigate("https://translate.yandex.com/")
in_text <- rd$findElement(using = "xpath",
                          value = "//div[@class='item item_left']
                          //textarea[@id='textarea']")

in_text$sendKeysToElement(list("Москва, Санкт-Петербург, Саратов", "\uE007"))
out_text <- rd$findElement(using = "xpath",
                           value = ".//*[@id='translation']")

out <- out_text$getElementText()
