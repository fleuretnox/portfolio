from pathlib import Path
from glob import glob
import pandas

# df = pandas.read_csv("", names=["Day", "Scheduled", "Tracked"])

# if Path(r'C:\Users\huhl\Desktop\devops\portfolio\dest_server').is_file():
#     print ("File exist")
# else:
#     print ("File not exist")
headers=["Day", "Scheduled", "Tracked"]

csv_files = glob.glob(r'C:\Users\Test\Excel\*.csv')
for csv_file in csv_files:
    df = pandas.read_csv(csv_file, names=headers)
    df ["Actual"] ="df[1] - df[2]"
    # Do something with each DataFrame here

df.to_csv("", index=False)
