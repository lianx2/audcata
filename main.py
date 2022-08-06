#!/usr/bin/python3

import gethttp as h
import subprocess as s
import sys
from os.path import exists
from os import system

# Files
# httpreq = "./.catalogs/{}".format(sys.argv[1])   # HTTP req file
# xslx = sys.argv[2]  # Excel spreadsheet to output
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
            #h.retrieveURL(val, httpreq)
            files.append(indivcat)
            print('[Progress] Could not find {}. Sending HTTP request...'.format(indivcat))
            h.retrieveURL(val, indivcat)
print('[Success] Retrieved data from all relevant webpages.')

# Compile individual catalogs for parsing in the next step.
unifiedname = './.catalogs/cat{}.txt'.format(''.join(nums))
#with open(unifiedname, 'a') as compiled:
#    for f in files:
#        with open(f, 'r') as indiv:
#            for line in indiv:
#                indiv.write(line)
#cmd = ['cat',] + files + ['>>', unifiedname]
filestr = ' '.join(files)
cmd = 'cat %s > %s' % (filestr, unifiedname)
system(cmd)

# Here, the HTTP request has been recieved in httpreq for the specified courses in num.txt
# Perl script to parse webscrape file for relevant data => txt
# s.call(["perl", "./parselog.pl", httpreq, xslx])
#s.call(["perl", "./parselog.pl", unifiedname, xslx])
cmd = 'perl ./parselog.pl %s %s' % (unifiedname, xslx)
system(cmd)
print('[Complete] Program terminated.')
