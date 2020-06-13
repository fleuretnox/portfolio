from selenium import webdriver
from time import sleep

#path for chromedriver
PATH = r'C:\Program Files\tmp\chromedriver.exe'
driver = webdriver.Chrome(PATH)

#Create a csv with given column

with open ('Extract_Server\May_Ext.csv', 'w') as createcsv:
    createcsv.write("Day Scheduled_Flights Tracked_Flights \n")

#Stat Site
driver.get('https://www.flightradar24.com/data/airports/jfk/statistics')

#To click the Burger Menu + View Table
driver.execute_script("window.scrollTo(0,600)")
sleep(3)
driver.find_element_by_class_name("highcharts-exporting-group").click()
ul = driver.find_element_by_class_name("highcharts-menu")
ul.find_elements_by_tag_name("li")[-1].click()

#Fetch Data by Inspecting the Element
table_list = driver.find_elements_by_xpath('//*[@id="highcharts-data-table-0"]/tbody')

#Until the end of the list
daily_flights = len(table_list)

#Append CSV
class Crawl:
    with open ('Extract_Server\May_Ext.csv', 'a') as createcsv:
        for crawl_list in range(daily_flights):
            createcsv.write(table_list[crawl_list].text)
            driver.close() #Close the browser

        print ("Data Has Been Extracted Successfully")
