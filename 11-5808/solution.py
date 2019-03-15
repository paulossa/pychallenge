# Solution for the URL http://www.pythonchallenge.com/pc/return/5808.html

# Hints: 
# Title of page says 'ODD EVEN' | Maybe two images interpolated? 

# USE PYTHON 3.6+ yo 
from PIL import Image

img = Image.open('cave.jpg')
pixels = img.load()

odd_x_img = Image.new('RGB', img.size)
even_x_img = Image.new('RGB', img.size)

x, y = img.size
for _y in range(y):
    for _x in range(x): 
        if (_x + _y) % 2 == 0: 
            even_x_img.putpixel((_x, _y), pixels[_x, _y])
        else:
            odd_x_img.putpixel((_x, _y), pixels[_x, _y])
#print(odd_x_img[0, 1])
even_x_img.save("even.jpg")
odd_x_img.save("odd.jpg")
print(pixels[0, 1])