import numpy  as np
from fbprophet import Prophet
import matplotlib.pyplot as plt

#for anaconda
# conda install -c conda-forge fbprophet

#import data for Per Usage
cpuuse = pd.read_csv (r'C:\Users\huhl\Desktop\devops\portfolio\load_server\may_ldg.csv')


###define df
df = pd.DataFrame()
df['ds'] = permuse['Day']
df['y'] = permuse['Tracked_Flights']


###create prophet class
class_model = Prophet()
class_model.fit(df)


###future prediction data frame
future = class_model.make_future_dataframe(periods=5, freq = 'm')

###forecasting
forecast = class_model.predict(future)

###plotting forecast
plot1 = class_model.plot(forecast)



df.to_csv(r'C:\Users\huhl\Desktop\devops\portfolio\load_server\may_ldg2.csv', index=False)
