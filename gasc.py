"""
Copyright (C) 2013 Frederick Roth

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import urllib.request
import urllib.parse
import re
import csv
from bs4 import BeautifulSoup

user_agent = (
    'Mozilla/5.0 (X11; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0'
)
headers = {'User-Agent': user_agent, }
urltemplate = (
    'https://www.google.de/search?q=%22{name}%22&lr=lang_de&safe=off&'
    'as_qdr=all&sa=X&source=lnt&tbs=lr%3Alang_1de%2Ccdr%3A1%2Ccd_min'
    '%3A{mindate}%2Ccd_max%3A{maxdate}&tbm='
)

searchterms = [urllib.parse.quote(line.strip()) for line in open('searchterm')]
timeranges = [line.split() for line in open('timeranges')]

outfile = open('results.csv', "w")
writer = csv.writer(outfile)
header = ['Player']
for r in timeranges:
    header.append(r[0] + '-' + r[1])
writer.writerow(header)
for term in searchterms:
    row = [term]
    for timerange in timeranges:
        url = urltemplate.format(
            name=term,
            mindate=timerange[0],
            maxdate=timerange[1]
        )
        print(url)

        request = urllib.request.Request(url, None, headers)
        response = urllib.request.urlopen(request)

        html = response.read()
        soup = BeautifulSoup(html)
        result = soup.find(id="resultStats")
        if result is not None:
            resultString = result.getText()
            m = re.search('([0-9.]+) ', resultString)
            dotnumber = m.group(1)
            plainnumber = dotnumber.replace('.', '')
            row.append(plainnumber)
    writer.writerow(row)
outfile.close()
