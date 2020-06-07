from bs4 import BeautifulSoup
import urllib.request

urlstat = 'https://www.flightradar24.com/data/airports/jfk/statistics'
urlreq = urllib.request.Request(urlstat, headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
urlpage = urllib.request.urlopen (urlreq)
#webresponse = urlopen('https://www.flightradar24.com/data/airports/jfk/statistics')
soup_mod = BeautifulSoup(urlpage, 'html.parser')

tableprint = soup_mod.find("div", class_="highcharts-data-table")


print (tableprint)
