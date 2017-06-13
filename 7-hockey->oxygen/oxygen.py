#coding: utf-8

from Tkinter import *

def getRGB(image, x, y):

    value = image.get(x, y)

    return value

def main():
    photo = PhotoImage(file="oxygen.png")
    cursor = 1
    lastGray = 0
    msg = ""
    while (cursor < photo.width()):
        tempLastGray = getRGB(photo, cursor, 47)[0]

        lastGray = tempLastGray
        msg += chr(lastGray)
        cursor += 7

    answer = [105, 110, 116, 101, 103, 114, 105, 116, 121]

    print msg
    print "Result = " + ''.join(map(chr, answer))

    for e in answer: print e, chr(e)

    # label = Label(root, image=photo)
    # label.grid()
    # root.mainloop()



root = Tk()
main()
