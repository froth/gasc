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
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
url = 'https://www.google.de/search?q=%22Frederick+Roth%22&lr=lang_de&safe=off&as_qdr=all&sa=X&ei=wmefUebRD6jL4ASu-YHQDw&ved=0CCMQpwUoBg&source=lnt&tbs=lr%3Alang_1de%2Ccdr%3A1%2Ccd_min%3A6.5.2013%2Ccd_max%3A24.5.2013&tbm='
headers={'User-Agent':user_agent,}
import urllib.request
import re
from bs4 import BeautifulSoup

request = urllib.request.Request(url,None,headers)
response = urllib.request.urlopen(request)

html = response.read()
soup = BeautifulSoup(html)

resultString = soup.find(id='resultStats').string
m = re.search(' ([0-9.]+) ', resultString)
dotnumber = m.group(1)
plainnumber = dotnumber.replace('.', '')
print(plainnumber)
