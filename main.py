#!/usr/bin/python3

import gethttp as h
import sys
from os.path import exists
from os import system

# Files
xslx = sys.argv[1]
nums = []
files = []

# Retrieve course numbers => retrieve URL data...
with open('num.txt', 'r') as f2o:
    for num in f2o:
        val = num.strip()
        nums.append(val)
        indivcat = './.catalogs/cat{}.txt'.format(val)
        # Check if a catalog already exists for that course number.
        if exists(indivcat):
            files.append(indivcat)
            print('[Success] Found {}. No need to send an HTTP request.'.format(indivcat))
            pass
        else:
            # If the file does not exist, HTTP request.
            files.append(indivcat)
            print('[Progress] Could not find {}. Sending HTTP request...'.format(indivcat))
            h.retrieveURL(val, indivcat)
print('[Success] Retrieved data from all relevant webpages.')

# Compile individual catalogs for parsing in the next step.
unifiedname = './.catalogs/cat{}.txt'.format(''.join(nums))
filestr = ' '.join(files)
cmd = 'cat %s > %s' % (filestr, unifiedname)
system(cmd)

# Here, the HTTP request has been recieved in httpreq for the specified courses in num.txt
# Perl script to parse webscrape file for relevant data => txt
cmd = 'perl ./parselog.pl %s %s' % (unifiedname, xslx)
system(cmd)
print('[Complete] Program terminated.')
