#
# A quick dirty timezone list scraper from  http://en.wikipedia.org/wiki/List_of_time_zone_abbreviations
#

import requests
from BeautifulSoup import BeautifulSoup
from pprint import pprint

html = requests.get('http://en.wikipedia.org/wiki/List_of_time_zone_abbreviations')
parser = BeautifulSoup(html.content)
table = parser.find('table', {"class":"wikitable sortable"})
resultList = []
for row in table.findAll('tr'):
    cols = row.findAll('td')
    result = {}
    for content in cols:
        res = content.find('a', href=True)
        if res:
            str = res.text
            value = ''
            label = ''

            if '+' in str and ':' in str:
                value = '+' + str.split('+')[1]
                result['value'] = value
            elif '+' in str:
                value = '+' + str.split('+')[1] + ':00'
                result['value'] = value
            else:
                label = str
                result['label'] = label

            if 'label' in result and 'value' in result:
                resultList.append(result)
                result = {}

pprint(resultList)
