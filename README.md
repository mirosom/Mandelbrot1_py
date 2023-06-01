# Mandelbrot1_py

 verified (tried out, to be exact) by me: miro holec, 01.06.2023
 source: https://medium.com/swlh/visualizing-the-mandelbrot-set-using-python-50-lines-f6aa5a05cf0f
 author: Blake Sanie
 Date: Nov 24, 2020

 Zn+1 = Zn**2 + C
 C = a + b*i
 begin with Zn = 0. Zn+1 = 0**2 + C = C
 Zn+1= (a + b*i)**2 + (a + b*i)

 (a + b*i)**2 = a**2 + 2*a*b*i + b**2 * i**2    #### (-1)**0.5**2 = -1
 therefore (a * b*i)**2 = a**2 +2abi - b**2 = (a**2 - b**2) +2abi = a new complex number
 and watching out, when it shall diverge, after how many iterations (coloring issue)
