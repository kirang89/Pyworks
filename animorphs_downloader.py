#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Script to download entire animorphs series
#

import requests
from urllib import quote

URL = 'http://downloads.animorphsforum.com/books/pdf/'

ORIGINAL_SERIES = [str(number) for number in range(1, 55)]
MEGAMORPHS = ['Megamorphs1', 'Megamorphs2', 'Megamorphs3', 'Megamorphs4']
OTHERS = ['Andalite', 'Ellimist', 'Visser', 'Hork-Bajir', 'Alternamorphs01', 'Alternamorphs02', 'Vegemorphs']

CHAPTERS = ORIGINAL_SERIES + MEGAMORPHS + OTHERS

def get_book():
    """ Construct urls for each chapter"""
    for chapter in CHAPTERS:
        name = chapter + ".pdf"
        url = URL + book
        yield url, book_name

if __name__ == '__main__':
    for book_url, book_name in get_book():
        print "Downloading {}".format(book_name)
        safe_url = quote(book_url, safe="%/:.")
        file = open(book_name, 'wb')
        response = requests.get(safe_url)

        for chunk in response.iter_content(1024):
            # Write chunk to file
            file.write(chunk)

        file.close()
        print "Downloaded {}".format(book_name)
