from pathlib import Path
import glob
import pandas as pd

#Fetch csv file (pretend the filename is unknown)
csv_files = glob.glob('Transform_Server\*.csv')

#For Application Layer, add an Accuracy Formula column
class Load:
    for load_csv_file in csv_files:
        df = pd.read_csv(load_csv_file)
        df ["Accuracy"] = (((df["Tracked_Flights"])/(df["Scheduled_Flights"]))*100)
        df.to_csv('Load_Server\May_Ldg.csv', index=False)


print ("It Has Been Loaded Successfully")






# df = pandas.read_csv("", names=["Day", "Scheduled", "Tracked"])

# if Path(r'C:\Users\huhl\Desktop\devops\portfolio\dest_server').is_file():
#     print ("File exist")
# else:
#     print ("File not exist")
# headers=["Day" "Scheduled" "Tracked"]
#
# csv_files = glob.glob(r'C:\Users\Test\Excel\*.csv')
# for csv_file in csv_files:
#     df = pandas.read_csv(csv_file, names=headers)
    # df ["Actual"] ="df[1] - df[2]"
    # Do something with each DataFrame here

# df.to_csv("", index=False)
