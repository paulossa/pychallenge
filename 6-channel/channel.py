# import zipfile
from zipfile import ZipFile
import re

def main():
    czip = ZipFile('channel.zip', 'r')
    for name in czip.namelist():
        if (name == 'readme.txt'): print czip.read(name)

    nothing = '90052'
    while True:
        fileContent = czip.read(nothing + '.txt')
        print czip.getinfo(nothing + '.txt').comment,
        match = re.findall('\d{2,5}', fileContent)
        if len(match) == 0: break
        else: nothing = match[0]

main()
