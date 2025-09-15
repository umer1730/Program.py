import requests
import json
import pyttsx3

city = input("Enter the name of the city:\n")

api_key = "YOUR_API_KEY"
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"


r = requests.get(url)

if r.status_code == 200:
    data = r.json()
    temp = data["current"]["temp_c"]
    print(f"Current temperature in {city}: {temp}°C")

    engine = pyttsx3.init()
    engine.say(f"The current temperature in {city} is {temp} degrees Celsius")
    engine.runAndWait()
else:
    print("Failed to retrieve weather data. Please check the city name or API key.")
