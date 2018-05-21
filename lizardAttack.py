import pip

def install(package):
    pip.main(['install', package])

install('imageio')
install('numpy')
install('Pillow')

import imageio
import numpy as np
from PIL import Image
import os
import urllib
import sys

if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve

urlretrieve("https://i.imgur.com/G1Sst10.png", "lizard.png")

ims = imageio.imread(os.getcwd()+"\\lizard.png")
print(ims.shape)
firstImage = Image.fromarray(ims,'RGB')
for i in range(2000):
	firstImage.show()