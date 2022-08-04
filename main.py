#!/usr/bin/python3

import gethttp as h
import subprocess as s
import sys

# Files
httpreq = "./.catalogs/{}".format(sys.argv[1])   # HTTP req file
xslx = sys.argv[2]  # Excel spreadsheet to output

# Retrieve course numbers => retrieve URL data...
with open('num.txt', 'r') as f2o:
    for num in f2o:
        val = num.strip()
         # Append URL contents to a text file...
        h.retrieveURL(val, httpreq)
print('[Success] Retrieved data from all relevant webpages.')

# Here, the HTTP request has been recieved in httpreq for the specified courses in num.txt
# Perl script to parse webscrape file for relevant data => txt
s.call(["perl", "./parselog.pl", httpreq, xslx])
print('[Complete] Program terminated.')
