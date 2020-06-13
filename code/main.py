from crawl import *
from transform import *
from load import *
# from forecasting import *
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

class DR_Move:
      try:
         backup_path
      except TypeError:
         print ("DR Backup Has Failed")
