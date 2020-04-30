import sys
import numpy
from PIL import Image, ImageDraw


if __name__ == '__main__':
    img = Image.open('background.jpg')
    new_img = img.resize((256,256))


    draw = ImageDraw.Draw(new_img)
    draw.line((0, 0) + new_img.size, fill=128)
    draw.line((0, new_img.size[1], new_img.size[0], 0), fill=128)
    del draw
    new_img.show()
    new_img.save('virusmapx','jpeg')
