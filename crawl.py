from selenium import webdriver
from time import sleep

PATH = r'C:\Program Files\tmp\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.flightradar24.com/data/airports/jfk/statistics')
driver.execute_script("window.scrollTo(0,600)")
sleep(5)
driver.find_element_by_class_name("highcharts-exporting-group").click()
ul = driver.find_element_by_class_name("highcharts-menu")
ul.find_elements_by_tag_name("li")[-1].click()


# driver = webdriver.Chrome()
# driver.get('https://www.flightradar24.com/data/airports/jfk/statistics')
# driver.execute_script("window.scrollTo(0,600)")
# sleep(5)
# driver.find_element_by_class_name("highcharts-exporting-group").click()

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
