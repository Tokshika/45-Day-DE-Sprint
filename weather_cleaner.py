import requests

cities = [
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "New York", "lat": 40.7128, "lon": -74.0060},
    {"name": "Tokyo", "lat": 35.6895, "lon": 139.6917}
]

for city in cities:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&current_weather=true"
    # 1. Fetch data
    # 2. Extract temperature
    # 3. Use if/elif/else to find the category (Hot/Cold/Mild)
    # 4. Print: "{city_name}: {temp}C - {category}"


git add weather_cleaner.py
git commit -m "Day 4: Implemented multi-city transformation logic"
git push
