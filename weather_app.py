import requests

API_KEY = "629dc0b23006fe40ff229ea65e686e93"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"Weather in {city}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Condition: {data['weather'][0]['description']}")
else:
    print("❌ Invalid city name or API key.")
    print(data)