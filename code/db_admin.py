import shutil
import glob
import pathlib

#CSV
csv_bkup_path = glob.glob('Backup Server\*.csv')
csv_dr_path = pathlib.Path('DR Server')

class CSV_MoveFile:
    for file in csv_bkup_path:
        shutil.copy(str(file), str(csv_dr_path))

print ("DR For CSV Has Been Backed Up Successfully")


#For Forecast Graph Backup
fcast_path = glob.glob('Forecasting_Server\*.png')
fcast_dr_path = pathlib.Path('Backup Server')

class Fcast_Backup_Migration:
    for file in fcast_path:
        shutil.copy(str(file), str(fcast_dr_path))

print ("Forecast Has Been Backed Up in Backup Server Successfully")

#For Forecast Graph DR
fcast_bkup_path = glob.glob('Backup Server\*.png')
fcast_dr_path = pathlib.Path('DR Server')

class Fcast_DR_Migration:
    for file in fcast_bkup_path:
        shutil.copy(str(file), str(fcast_dr_path))

print ("DR For Forecast Has Been Backed Up Successfully")
