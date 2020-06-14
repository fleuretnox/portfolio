from crawl import *
from transform import *
from load import *
from forecasting import *
from db_admin import *


#crawl.py
# crawl = Crawl()
# crawl_cfg = CrawlConfig()
#
class Extract:
     try:
        daily_flights
     except TypeError:
         print ("Crawling Stage Has Failed")


class Transform:
     try:
        trf_csv_files
     except TypeError:
         print ("Transforming Stage Has Failed")


class Load:
     try:
        ld_csv_files
     except TypeError:
         print ("Loading Stage Has Failed")


class Forecast:
     try:
        fcast_csv_files
     except TypeError:
         print ("Forecasting Has Failed")



class CSV_Backup:
      try:
         csv_bkup_path
      except TypeError:
         print ("CSV Backup Has Failed")


class Forecast_Backup:
      try:
         fcast_path
      except TypeError:
         print ("Forecast Backup Has Failed")


class Forecast_DR:
      try:
         fcast_bkup_path
      except TypeError:
         print ("Forecast DR Migration Has Failed")
