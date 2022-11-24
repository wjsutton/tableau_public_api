# From Stack Overflow
# https://stackoverflow.com/questions/7460218/get-image-size-without-downloading-it-in-python
# By using the requests library method:

import requests
from PIL import ImageFile

url = 'https://public.tableau.com/views/RunningforOlympicGold/RunningforOlympicGold.png?%3Adisplay_static_image=y&:showVizHome=n'

resume_header = {'Range': 'bytes=0-20000000'}    ## the amount of bytes you will download
data = requests.get(url, stream = True, headers = resume_header).content

p = ImageFile.Parser()
p.feed(data)    ## feed the data to image parser to get photo info from data headers
if p.image:
    # print(p.image.size) ## get the image size (Width, Height)
    # adjusting image dimensions
    # width is 1 pixel less than actual
    # height include 26 pixels of tableau footer
    width = p.image.size[0]+1
    height = p.image.size[1]-26
    print(width)
    print(height)
## output: (1250, 900)