from weather import get_weather
from datetime import datetime

def main ():

    cache = {}

    while True:
        while True:
            print("Please enter a city name or type 'exit' to quite.")
            user_input = input().lower().strip()

            if user_input:
                break
        
        if user_input == "exit":
            break
        else:
            if user_input in cache:
                weather = cache[user_input]
                print("fast retrieval activated")
                print("")
                print(f"City Name: {weather['city_name']}")
                print(f"Country: {weather['country']}")
                print(f"Weather Description: {weather['description']}")
                print(f"Temperature: {weather['temperature']}°C")
                print(f"Feels Like: {weather['feels_like']}°C")
                print(f"Minimum Temperature: {weather['temp_min']}°C")
                print(f"Maximum Temperature: {weather['temp_max']}°C")
                print(f"Pressure: {weather['pressure']} hPa")
                print(f"Humidity: {weather['humidity']}%")
                print(f"Sea Level Pressure: {weather['sea_level']} hPa")
                print(f"Ground Level Pressure: {weather['grnd_level']} hPa")
                print(f"Visibility: {weather['visibility']} meters")
                print(f"Wind Speed: {weather['wind_speed']} m/s")
                print(f"Sunrise: {weather['sunrise']}")
                print(f"Sunset: {weather['sunset']}")
                print(f"Date: {weather['date']}")
                print(f"Timezone Offset (seconds): {weather['timezone']}")
            else:
                print("fetching...Please wait!\n")
                data = get_weather(user_input)
                weather = data["data"]
                is_error = data["err"]
                if is_error:
                    print(is_error)
                else:
                    try:
                        description = weather["weather"][0].get("description" , "Not available!")
                        temperature = weather.get("main").get("temp" , "Not available")
                        feels_like = weather["main"]["feels_like"]
                        temp_min = weather["main"]["temp_min"]
                        temp_max = weather["main"]["temp_max"]
                        pressure = weather["main"]["pressure"]
                        humidity = weather["main"]["humidity"]
                        sea_level = weather["main"]["sea_level"]
                        grnd_level = weather["main"]["grnd_level"]
                        visibility = weather["visibility"]
                        wind_speed = weather["wind"]["speed"]   # ✅ fixed
                        country = weather["sys"]["country"]
                        sunrise = datetime.fromtimestamp(weather["sys"]["sunrise"])
                        sunset = datetime.fromtimestamp(weather["sys"]["sunset"])
                        date = datetime.fromtimestamp(weather["dt"])
                        timezone = weather["timezone"]
                        city_name = weather["name"]

                        print(f"City Name: {city_name}")
                        print(f"Country: {country}")
                        print(f"Weather Description: {description}")
                        print(f"Temperature: {temperature}°C")
                        print(f"Feels Like: {feels_like}°C")
                        print(f"Minimum Temperature: {temp_min}°C")
                        print(f"Maximum Temperature: {temp_max}°C")
                        print(f"Pressure: {pressure} hPa")
                        print(f"Humidity: {humidity}%")
                        print(f"Sea Level Pressure: {sea_level} hPa")
                        print(f"Ground Level Pressure: {grnd_level} hPa")
                        print(f"Visibility: {visibility} meters")
                        print(f"Wind Speed: {wind_speed} m/s")
                        print(f"Sunrise: {sunrise}")
                        print(f"Sunset: {sunset}")
                        print(f"Date: {date}")
                        print(f"Timezone Offset (seconds): {timezone}")
                        print("")

                        cache[user_input] = {
                                "city_name": city_name,
                                "country": country,
                                "description": description,
                                "temperature": temperature,
                                "feels_like": feels_like,
                                "temp_min": temp_min,
                                "temp_max": temp_max,
                                "pressure": pressure,
                                "humidity": humidity,
                                "sea_level": sea_level,
                                "grnd_level": grnd_level,
                                "visibility": visibility,
                                "wind_speed": wind_speed,
                                "sunrise": sunrise,
                                "sunset": sunset,
                                "date": date,
                                "timezone": timezone
                            }

                    except KeyError: 
                        print("Some data for your region is not available!")



if __name__ == "__main__":
    print("Welcome to weather cli!")
    main()