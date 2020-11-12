library(RCurl)
library(png)

screenshot <-'https://public.tableau.com/static/images/El/Election2020-TheRoadToBeingPOTUS/Election2020-TheRoadToBecomingPOTUS/1.png'
thumbnail <- 'https://public.tableau.com/thumb/views/Election2020-TheRoadToBeingPOTUS/Election2020-TheRoadToBecomingPOTUS'

# not working
image <-  readPNG(getURLContent(screenshot))
image <-  readPNG(getURLContent(thumbnail))

# download file option works
download.file(screenshot, "temp.png", mode = "wb")
localPNG <- readPNG("temp.png")
dim(localPNG)
file.remove("temp.png")

download.file(thumbnail, "temp.png", mode = "wb")
localPNG <- readPNG("temp.png")
dim(localPNG)
file.remove("temp.png")
