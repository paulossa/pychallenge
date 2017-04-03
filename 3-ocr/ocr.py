#coding: utf-8
from string import ascii_letters

def main():
    file_input = open("mess.txt", "r")
    mess = file_input.read() # this will have the text from the txt file


    # dictionary = {}
    #
    # for character in mess:
    #     if (character in dictionary.keys()): dictionary[character] += 1
    #     else: dictionary[character] = 1
    #
    # print dictionary
    # THE dictionary doesn't keep items in order but serves to show me what I'm
    # looking for.

    print ''.join([ c for c in mess if c in ascii_letters])


main()
