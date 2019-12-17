library(RSelenium)
library(sys)
library(devtools)

#install_github("omegahat/Rcompression")

fprof <- getFirefoxProfile("C:\\Users\\zahar\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\qwlmtfbp.selenium", useBase = TRUE)
rD <- rsDriver(remoteServerAddr = "localhost",
               port = 8895L,
               browser = "firefox",
               extraCapabilities = fprof)
rd <- rD[["client"]]

rd$open()
rd$navigate("https://www.epam.com/about")
rd$screenshot(display = TRUE)

webItem <- rd$findElement(
  using = "css selector",
  value = "a[href$='Corporate_Fact_Sheet_Global.pdf']"
)

Sys.sleep(3)

webItem$clickElement()

rd$close()
