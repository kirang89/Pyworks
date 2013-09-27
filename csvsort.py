#!/usr/bin/python

"""A simple script to sort csv data

Usage:
    csvsort.py <filename> --column=<cno>
    csvsort.py <filename> --column=<cno> --dest=<destination-file>
    csvsort.py <filename> --column=<cno> --desc
    csvsort.py <filename> --column=<cno> --desc --dest=<destination-file>
    csvsort.py (-h | --help)
    csvsort.py --version

Options:
    -h --help                   Display available commands
    --version                   Get the version
    --column=<cno>              The column number to be used for sorting
    --desc                      Sort in descending order
    --dest=<destination-file>   Write output data to file

"""

import csv
from operator import itemgetter
from docopt import docopt
from pprint import pprint

def gettypes(headers):
    types = []
    for name in headers:
        start = name.find("(")
        end = name.find(")")
        types.append(name[start+1:end])
    return types

def convert(types, row):
    return [eval(t)(val) for t, val in zip(types, row)]

def write_data_to_dest(headers, data, destination):
    with open(destination, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)


def sort_csv(csvfile,column, desc=False, destination=None):
    csvdata = []
    headers = []
    with open(csvfile, "rb") as f:
        for row in csv.reader(f):
            headers = row
            break

        types = gettypes(headers)
        count = 0
        for row in csv.reader(f):
            if count == 0:
                count = 1
            else:
                csvdata.append(convert(types,row))
    if desc:
        csvdata.sort(key=itemgetter(*column), reverse=True)
    else:
        csvdata.sort(key=itemgetter(*column))

    if not destination:
        print "Data sorted based on column {}".format(column)
        print "---------------------------------"
        pprint(csvdata)
    else:
        write_data_to_dest(headers, csvdata, destination)

if __name__ == "__main__":
    arguments = docopt(__doc__, version="csvsort-0.1")
    desc = arguments['--desc']
    carg = arguments['--column']
    if carg.find(",") > 0:
        cols = [int(val)-1 for val in carg.split(",")]
    else:
        cols = list(int(carg)-1)

    if arguments.has_key('--dest'):
        dest = arguments['--dest']
    else:
        dest = None

    sort_csv(arguments["<filename>"], cols, desc, dest)
