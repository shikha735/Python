import random
import urllib.request

def download_image(url):
    name = random.randrange(1, 1000)
    file_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, file_name)

download_image("http://photos.filmibeat.com/ph-big/2013/03/yeh-jawani-hai-deewani_13636919600.jpg")