# Tested on Raspberry Pi 4 Model B
# Huats Club 2022 for the Pixel-Tint Project
from PIL import Image, ImageOps
from student_pub import *

## open image file
myImage = Image.open('horoscope pics')
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
