import numpy  as np
from fbprophet import Prophet
import glob
import pandas as pd
from matplotlib import pyplot as plt
#Fetch csv file (pretend the filename is unknown)
fcast_csv_files = glob.glob('Extract_Server\*.csv')

class Forecast:
    for begin in fcast_csv_files:
# #DataFrame Class
# class Dataframe:
        df = pd.DataFrame()
        df['ds'] = pd.to_datetime(fcast_csv_files['Day'])
        df['y'] = fcast_csv_files['Tracked_Flights']


# class For_Prophet:
        class_model = Prophet()
        class_model.fit(df)


#Period and Frequency of Forecasting



# class Forecast:
        df=df.rename(columns={'ds':'Date', 'y':'Track'}) #rename ds and y columns
        future = class_model.make_future_dataframe(periods=30, freq = 'd')
        forecast = class_model.predict(future)
        plot1 = class_model.plot(forecast)
        plot1.savefig("May_Forecast_Graph.png", dpi=72)
