#!/usr/bin/python3

import requests
# import xlsxwriter

def retrieveURL(num, httpreq):
    """
    num: int, course/major number (i.e. 5, 6, etc.)
    httpreq: string, output file
    appends webpage contents to <httpreq>
    """
    # Retrieve the data from input URL...
    course = str(num)
    url = 'http://student.mit.edu/catalog/m{}a.html'.format(course)
    print('[Initializing] Retrieving url = {}'.format(url))
    data = requests.get(url)

    # Append data to catalog.txt
    with open(httpreq, 'a') as f2a:
        f2a.write(data.text)
    print('[Success] Data from {} retrieved.'.format(url))
    return


# def excel(f2w, lines):
#    """
#    f2w: string, name of excel file to output
#    line: list of lists; each list element is a row of data
#    creates and formats an excel spreadsheet with course data
#    """
#    # Initialize the workbook...
#    print('[Initializing] Creating workbook {}...'.format(f2w))
#    workbook = xlsxwriter.Workbook(f2w)
#    worksheet = workbook.add_worksheet()
#    # Write data contents...
#    print('[Progress] Writing data to {}...'.format(f2w))
#    row = 0
#    col = 0
#    for r in range(len(lines)):
#        for c in range(len(lines[r])):
#            worksheet.write(row, col, lines[r][c])
#    workbook.close()
#    print('[Success] Data written to {}!'.format(f2w))
#    return
