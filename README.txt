# Parses select MIT course catalogs for specific course
# attributes and generates an Excel file with the data.

# Author: jlian@cecil
# Creation: 20220803

##################################
FILES

main.py     => main execution, data piping, shell command
gethttp.py  => HTTP request to specified URLs; returns .txt file (httpreq)
parselog.pl => parses httpreq for specified course attributes; returns .xlsx file (xlsx)
num.txt     => holds MIT course numbers for HTTP request

##################################
ASSOCIATED CMDS, ALIASES

$ mitlog [httpreq] [xlsx]   => executes main.py
$ bucket [file]             => moves files to winbucket

    supplemental: apd, rmf => append, remove from num.txt

##################################
DATA FLOW

main.py [httpreq] [xlsx]
    -> gethttp.py [num.txt]
        -> [httpreq].txt
    -> parselog.pl [httpreq]
        -> [xlsx].xlsx

1) main.py is called with two file arguments
2) gethttp.py is called to get HTTP from the sites specified in num.txt
3) main.py calls parselog.pl
4) parselog.pl parses for specific course attirbutes
5) parselog.pl generates an .xlsx file with a specific format

20220805 NOTE: main.py now checks if an HTTP request has already been sent for a specific
course number. If it has, main.py does no request another. The selected catalogs are compiled
for parsing (httpreq).

##################################
COURSE ATTRIBUTES perl

@crn        => course number
@title      => course title/name
@units      => units
@total      => sum of units
@instructor => instructor

##################################
EXAMPLE OUTPUT
20220803: https://user-images.githubusercontent.com/69220047/182772454-4087e5e9-ad3c-48d5-9264-3827d448f0df.png
20220805: https://user-images.githubusercontent.com/69220047/183227952-d8dffb9a-ba4f-4ef4-80ed-3ca9a0d270ba.png

