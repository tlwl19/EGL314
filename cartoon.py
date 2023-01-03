# Tested on Raspberry Pi 4 Model B
# Huats Club 2022 for the Pixel-Tint Project
from PIL import Image, ImageOps
from student_pub import *
import os

path = os.path.abspath('horoscope pics') + '\\Aries.png' #edit 2 to the name of 25% pic
files = path.replace('\\','/')

## open image file
myImage = Image.open(files)
myImage.show()

## greyscale image file
greyImage = ImageOps.grayscale(myImage)
#greyImage.show()

## Limiting to 8 shades of greyscale colour
greyQuantize = greyImage.quantize(8)
#greyQuantize.show()

## resize to 32 x 32 pixels
smallImage = greyQuantize.resize((32,32), Image.BILINEAR)
#smallImage.show()

## Blow it back up to original photo size (32 x 32 pixels upscale)
resultImage = smallImage.resize(myImage.size, Image.NEAREST)
resultImage.show()

## Write Image to save .png file
#resultImage.save('cartoon.png')

# Retrieving pixel value and formating it into list of list
