import requests

# Open-Meteo is a free API that doesn't need a key
url = "https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current_weather=true"

response = requests.get(url)
data = response.json()

# Extract the temperature
temp = data['current_weather']['temperature']
print(f"The current temperature in London is {temp} degrees.")

git add .
git commit -m "Day 3: First successful API extraction and SQL Join solved"
  git push
