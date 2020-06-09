from pathlib import Path
import glob
import pandas as pd

#headers=["Day", "Scheduled", "Tracked"]
# csv_files = glob.glob(r"C:\Users\huhl\Desktop\devops\portfolio\test2.csv")
# for csv_file in csv_files:
csv_files = glob.glob(r'C:\Users\huhl\Desktop\devops\portfolio\extract_server\*.csv')
for csv_file in csv_files:
    df = pd.read_csv(csv_file, delimiter=' ')
    df.to_csv(r'C:\Users\huhl\Desktop\devops\portfolio\transform_server\may_tx.csv', index=False)
    print ("It's Transformed")
