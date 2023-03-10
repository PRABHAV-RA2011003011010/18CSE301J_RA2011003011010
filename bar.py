import os
os.chdir(r'C:\xampp\htdocs\data')
car_sales = pd.read_csv('pollution3.csv')
car_sales.head()
manufacturer = car_sales['Country']
sales = car_sales['NO2 AQI Value']
o=car_sales['CO AQI Value']
fig = plt.figure(figsize=(15,10))
plt.bar(manufacturer, sales,color='purple')
plt.bar(manufacturer, o,color='green')
plt.xlabel('Country')
plt.ylabel('AQIValue(NO2 AQI Value+CO AQI Value)')


plt.title('Comparision of CO and NO2 AQIValues of different Countries ')
plt.show()
