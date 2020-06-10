import numpy  as np
from fbprophet import Prophet
import glob
import pandas as pd
#Fetch csv file (pretend the filename is unknown)
csv_files = glob.glob('Extract_Server\*.csv')

#DataFrame Class
class Dataframe:
    df = pd.DataFrame()
    df['ds'] = pd.to_datetime(csv_files['Day'])
    df['y'] = csv_files['Tracked_Flights']

#
class For_Prophet:
    class_model = Prophet()
    class_model.fit(df)


#Period and Frequency of Forecasting



class Forecast:
    future = class_model.make_future_dataframe(periods=30, freq = 'd')
    forecast = class_model.predict(future)
    plot1 = class_model.plot(forecast)

class Plot_Forecast:
    df.to_csv('Forecasting_Server\May_Forecast.csv', index=False)

class BackUp:
    df.to_csv('Backup Server\May_Forecast_Backup.csv', index=False)
