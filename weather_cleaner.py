import requests
import csv
import time
from datetime import datetime

cities = [ 
    {"name": "London", "lat": 51.5074, "lon": -0.1278}, 
    {"name": "New York", "lat": 40.7128, "lon": -74.0060}, 
    {"name": "Tokyo", "lat": 35.6895, "lon": 139.6917}
]

print("Starting the Weather ETL Engine... (Press Ctrl+C to stop)")

while True:
    print(f"\n--- Starting Data Fetch at {datetime.now().strftime('%H:%M:%S')} ---")
    
    for city in cities: 
        url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&current_weather=true"  
        
        try:
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

            print(f"  > {city['name']}: {temp}°C ({category})")

            # 3. SAVE to CSV 
            with open('weather_data.csv', 'a', newline='') as f: 
                writer = csv.writer(f) 
                writer.writerow([city['name'], temp, category, datetime.now()])

        except Exception as e:
            print(f"  ! Error fetching {city['name']}: {e}")

    print("Cycle complete. Waiting 60 seconds...")
    time.sleep(60)London,11.2,Cold,2026-03-23 19:04:08.201664
New York,2.9,Cold,2026-03-23 19:04:09.126675
Tokyo,9.2,Cold,2026-03-23 19:04:10.481863
London,11.2,Cold,2026-03-23 19:05:12.217386
New York,2.9,Cold,2026-03-23 19:05:13.654234
Tokyo,9.2,Cold,2026-03-23 19:05:15.201701
London,11.2,Cold,2026-03-23 19:06:16.642152
New York,2.9,Cold,2026-03-23 19:06:18.177518
Tokyo,9.2,Cold,2026-03-23 19:06:19.689591
London,11.2,Cold,2026-03-23 19:07:21.156781
New York,2.9,Cold,2026-03-23 19:07:22.669007
Tokyo,9.2,Cold,2026-03-23 19:07:24.316640
London,11.2,Cold,2026-03-23 19:08:25.873735
New York,2.9,Cold,2026-03-23 19:08:27.389348
Tokyo,9.2,Cold,2026-03-23 19:08:28.841592
