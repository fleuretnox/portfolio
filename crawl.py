from selenium import webdriver
from time import sleep


PATH = r'C:\Program Files\tmp\chromedriver.exe'

url = 'https://github.com/fleuretfreya/portfolio'
with open (r'C:\Users\huhl\Desktop\devops\portfolio\extract_server\may_ext.csv', 'w') as createcsv:
     createcsv.write("Day Scheduled_Flights Tracked_Flights \n")

driver = webdriver.Chrome(PATH)

driver.get('https://www.flightradar24.com/data/airports/jfk/statistics')
driver.execute_script("window.scrollTo(0,600)")
sleep(3)
driver.find_element_by_class_name("highcharts-exporting-group").click()
ul = driver.find_element_by_class_name("highcharts-menu")
ul.find_elements_by_tag_name("li")[-1].click()

# rows = driver.find_elements_by_tag_name('th')


#table_list = driver.find_elements_by_tag_name('thead')
table_list = driver.find_elements_by_xpath('//*[@id="highcharts-data-table-0"]/tbody')
#table_list2 = driver.find_elements_by_xpath('//*[@id="highcharts-data-table-0"]/thead/tr/th[2]')

num_of_flights = len(table_list)
with open (r'C:\Users\huhl\Desktop\devops\portfolio\extract_server\may_ext.csv', 'a') as createcsv:
        for iteration_list in range(num_of_flights):
            createcsv.write(table_list[iteration_list].text)
            driver.close()
