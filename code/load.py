from pathlib import Path
import glob
import pandas as pd

#Fetch csv file (pretend the filename is unknown)
ld_csv_files = glob.glob('Transform_Server\*.csv')

#For Application Layer, add an Accuracy Formula column
class Load:
    for load_csv_file in ld_csv_files:
        df = pd.read_csv(load_csv_file)
        df ["Accuracy"] = (((df["Tracked_Flights"])/(df["Scheduled_Flights"]))*100)
        df.to_csv('Load_Server\May_Ldg.csv', index=False)
        df.to_csv('Backup Server\May_Ldg.csv', index=False) #CSV Backup

print ("It Has Been Loaded Successfully")
print ("It Has Been Backed Up Successfully")
