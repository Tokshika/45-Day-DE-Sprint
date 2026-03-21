weather_data.csv

import requests
import csv
from datetime import datetime

cities = [ 
    {"name": "London", "lat": 51.5074, "lon": -0.1278}, 
    {"name": "New York", "lat": 40.7128, "lon": -74.0060}, 
    {"name": "Tokyo", "lat": 35.6895, "lon": 139.6917}
]

for city in cities: 
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&current_weather=true"  
    
    # 1. Fetch data 
    response = requests.get(url) 
    data = response.json() 
    temp = data['current_weather']['temperature']  
    
    # 2. Categorize (The Logic) 
    if temp > 25: 
        category = "Hot" 
    elif temp < 15: 
        category = "Cold" 
    else: 
        category = "Mild"

    # THIS PART MUST BE INDENTED (Inner block of the loop)
    print(f"{city['name']}: {temp}°C - {category}")

    # 3. SAVE to CSV (The 'Load' part of ETL) 
    with open('weather_data.csv', 'a', newline='') as f: 
        writer = csv.writer(f) 
        writer.writerow([city['name'], temp, category, datetime.now()])
