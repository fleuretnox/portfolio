from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = r'C:\Program Files\tmp\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.melbourneairport.com.au/Passengers/Flights/Arrivals')

arrival_date = driver.find_elements_by_xpath('//div[@class="arrival_table_field arrival_date"]')
arrival_code = driver.find_elements_by_xpath('//div[@class="arrival_table_field arrival_code"]')

with open (r'C:\Users\huhl\Desktop\devops\portfolio\test.csv', 'w') as createcsv:
    createcsv.write("Day, Scheduled, Tracked \n")

num_of_flights = len(arrival_date)

with open (r'C:\Users\huhl\Desktop\devops\portfolio\test.csv', 'a') as createcsv:
        for iteration_list in range(num_of_flights):
            createcsv.write(arrival_date[iteration_list].text + " : " + arrival_code[iteration_list].text)



driver.close()
# import bs4
# import requests
# from bs4 import BeautifulSoup
#
#
# r = requests.get('https://www.flightradar24.com/data/airports/jfk/statistics')
# soup = bs4.BeautifulSoup(r.text, "xml")
#
# soup
# # soup.find_all('div', {"class:" 'highcharts-data-table'})
# urlstat = 'https://www.flightradar24.com/data/airports/jfk/statistics'
# urlreq = urllib.request.Request(urlstat, headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
# urlpage = urllib.request.urlopen (urlreq)
# #webresponse = urlopen('https://www.flightradar24.com/data/airports/jfk/statistics')
# soup_mod = BeautifulSoup(urlpage, 'html.parser')
#
# tableprint = soup_mod.find("div", class_="highcharts-data-table")
#
#
# print (tableprint)
