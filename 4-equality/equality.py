#coding: utf-8
from urllib2 import urlopen
import re

def main():
    url = "http://www.pythonchallenge.com/pc/def/equality.html"
    req = urlopen(url)
    pageSrc = req.read()

    matcher = re.search('<!--([\n\w]+)-->', pageSrc)
    text  =  matcher.group(1)


    result = re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', text)
    print ''.join(result)

main()
