from pathlib import Path
import glob
import pandas as pd

#Fetch csv file (pretend the filename is unknown)

trf_csv_files = glob.glob('Extract_Server\*.csv')

#Delimeting for each column
class Transform:
    for trf_csv_file in trf_csv_files:
        df = pd.read_csv(trf_csv_file, delimiter=' ')
        df.to_csv('Transform_Server\May_Trf.csv', index=False)

    print ("Data Has Been Transformed Successfully")


##remove unnamed3
