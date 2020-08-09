#Get update data from API
#Create data fram
#plot
import requests
import pandas as pd
import matplotlib.pyplot as plt

r = requests.get('https://covid19.th-stat.com/api/open/timeline')
j = r.json()
f = pd.DataFrame(j)
Data = f["Data"].tolist()
datafram = pd.json_normalize(f['Data'])


plt.figure(figsize=(10,5)) #size x,y
multi = plt.gca()
datafram.plot(kind='line',x='Date',y='Confirmed',color='blue',ax=multi)
datafram.plot(kind='line',x='Date',y='Recovered',color='green',ax=multi)
datafram.plot(kind='line',x='Date',y='Deaths',color='red',ax=multi)
datafram.plot(kind='line',x='Date',y='Hospitalized',color='yellow',ax=multi)
plt.suptitle('Covid19 Timeline')
plt.grid(True)
plt.show()

