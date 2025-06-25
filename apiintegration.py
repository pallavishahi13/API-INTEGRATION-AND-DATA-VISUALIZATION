import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


API_KEY = "your_api_key_here"
CITY = "Delhi"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"


response = requests.get(URL)
data = response.json()


dates = []
temperatures = []

for item in data['list']:
    dt_txt = item['dt_txt']
    temp = item['main']['temp']
    
    dates.append(datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S"))
    temperatures.append(temp)


plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temperatures, marker='o', color='orange')
plt.title(f"5-Day Weather Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
