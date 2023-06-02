

# verified (tried out, to be exact) by me: miro holec, 01.06.2023
# source: https://medium.com/swlh/visualizing-the-mandelbrot-set-using-python-50-lines-f6aa5a05cf0f
# author: Blake Sanie
# Date: Nov 24, 2020
# modified by: miro holec, Jun 01, 2023

# Zn+1 = Zn**2 + C
# C = a + b*i
# begin with Zn = 0. Zn+1 = 0**2 + C = C
# Zn+1= (a + b*i)**2 + (a + b*i)

# (a + b*i)**2 = a**2 + 2*a*b*i + b**2 * i**2    #### (-1)**0.5**2 = -1
# therefore (a * b*i)**2 = a**2 +2abi - b**2 = (a**2 - b**2) +2abi = a new complex number
# and watching out, when it shall diverge, after how many iterations (coloring issue)

from PIL import Image # pillow image processing library 
import colorsys
import math
import os
import platform

width = 600 #pixels
x = -0.65
y = 0
xRange = 3.4
aspectRatio = 4/3

precision = 100 # number of iterations

height = round(width / aspectRatio)
yRange = xRange / aspectRatio
minX = x - xRange / 2
maxX = x + xRange / 2
minY = y - yRange / 2
maxY = y + yRange / 2


#             |
#             |
#             |
#             |
# ------------0------------ x + xRange/2
#             |
#             |
#             |
#             | y - yRange / 2

img = Image.new('RGB', (width, height), color = 'black') 
pixels = img.load() 

def logColor(distance, base, const, scale):
    color = -1*math.log(distance,base)
    rgb = colorsys.hsv_to_rgb(const+scale*color,0.8, 0.9)
    return tuple(round(i*255) for i in rgb)

def powerColor(distance,exp,const,scale):
    color = distance**exp
    rgb = colorsys.hsv_to_rgb(const+scale*color, 1-0.6*color,0.9)
    return tuple(round(i*255) for i in rgb)

# MANDELBROT RENDERING ALGORITHM
#	escape time algorithm
# we loop through the image's pixels, and map each pixel to a cartesian
# point (x,y). The original x and y values are stored for later use

for row in range(height):
    for col in range(width):
        x = minX + col*xRange/width # xRange * (col / width) # pixel position ratio, translated to xRange
        y = maxY - row * yRange / height # maybe because bmp is upside down and we are counting from up
        oldX = x
        oldY = y
        
        for i in range(precision + 1):
            a = x*x - y*y # real component of z^2
            b = 2*x*y     # imaginary component of z^2
            x = a + oldX  # real component of new z
            y = b + oldY  # imaginary component of new z
            if x*x + y*y > 4: # divergent
                break
            
            if i < precision:
                distance = (i+1) / (precision + 1) # ratio again, reached percentage of precision
                rgb = powerColor(distance, 0.2, 0.27, 1.0)
                pixels[col,row] = rgb
            index = row * width + col + 1
            #print("{} / {}, {}%".format(index, width * height, round(index / width / height * 100 * 10)/10))




img.save('output.png')
if platform.system() == 'Windows':
    os.system('start output.png')
else:
    os.system('open output.png')





