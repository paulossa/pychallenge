# coding: utf-8
from PIL import Image

def main():
    img = Image.open('oxygen.png')
    pix = img.load()
    width, height = img.size
    result = []
    for i in range(3, width, 7):
        result.append(chr(pix[i, height/2][0]))
    print(''.join(result))
    ans = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    print(''.join( map(chr, ans) ))




#root = Tk()
main()
