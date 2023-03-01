
import os
import sys
from PIL import Image
import numpy as np
import microscope as ms

TRANSFORM = (100, 65, 200)
VECTOR = (3,3,3)
THRESHOLD = 50

# Specify image path and open image
image_file = "cholesterol project\\cholesterol drug screening in scc47\\drug treatment for 24 hours during invasion10_11_22\\A939572 _lower chamber treatment\\jpeg\\10uM-1.jpg"
im = Image.open(image_file)

#Retrieve data from image and close
size = im.size
data = list(im.getdata())
im.close()

# Create binary pixel array
n = len(data)
pixels = [(255,255,255)]*n

found = 0
for i in range(n):
    if ms.closeDist(data[i], TRANSFORM, VECTOR) < THRESHOLD:
        pixels[i] = (0,0,0)
        found += 1


out_image = Image.new(im.mode,im.size)
out_image.putdata(pixels)

out_image.save("test.jpg")

print((found*1.0)/n)
