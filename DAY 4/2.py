#weather information

import requests

def weather(city,api_key):
     
      
       url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

       try:
           response=requests.get(url)
           response.raise_for_status()
           data = response.json()

           temperature=data["main"]["temp"]
           humidity=data["main"]["humidity"]
           feels_like=data["main"]["feels_like"]
           print(f"weather in {city}: ")
           print(f"temperature :{temperature}: ")
           print(f"humidity :{humidity}")
           print(f"Description :{data["weather"][0]["description"].capitalize()}")
       except  requests.exceptions.RequestException as e :
                 print(f"Error fetching weather data : {e}" )



city=input("enter city name : ")
api_key="728641ab27bcdf8ed6adb5284d20ab88"
weather(city,api_key)


