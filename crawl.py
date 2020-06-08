from selenium import webdriver
from time import sleep

PATH = r'C:\Program Files\tmp\chromedriver.exe'

with open (r'C:\Users\huhl\Desktop\devops\portfolio\test2.csv', 'w') as createcsv:
    createcsv.write("Day, Scheduled, Tracked \n")

driver = webdriver.Chrome(PATH)

driver.get('https://www.flightradar24.com/data/airports/jfk/statistics')
driver.execute_script("window.scrollTo(0,600)")
sleep(3)
driver.find_element_by_class_name("highcharts-exporting-group").click()
ul = driver.find_element_by_class_name("highcharts-menu")
ul.find_elements_by_tag_name("li")[-1].click()


table_list = driver.find_elements_by_xpath('//div[@class="highcharts-data-table"]')

num_of_flights = len(table_list)

with open (r'C:\Users\huhl\Desktop\devops\portfolio\test2.csv', 'a') as createcsv:
        for iteration_list in range(num_of_flights):
            createcsv.write(table_list[iteration_list].text)
