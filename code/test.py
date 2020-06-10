from selenium import webdriver
from time import sleep

PATH = r'C:\Program Files\tmp\chromedriver.exe'

url = 'https://github.com/fleuretfreya/portfolio'
with open ('url/may_ext.csv', 'w') as createcsv:
     createcsv.write("Day Scheduled_Flights Tracked_Flights \n")
