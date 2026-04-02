from weather import get_weather
from datetime import datetime

def main ():
    while True:
        while True:
            print("Please enter a city name or type 'exit' to quite.")
            user_input = input()

            if user_input:
                break
        
        if user_input == "exit":
            break
        else:
            print("fetching...Please wait!\n")
            data = get_weather(user_input)
            weather = data["data"]
            is_error = data["err"]
            if is_error:
                print(is_error)
            else:
                description = weather["weather"][0]["description"]
                temperature = weather["main"]["temp"]
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
                sunrise = weather["sys"]["sunrise"]
                sunset = weather["sys"]["sunset"]
                date = weather["dt"]
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
                print(f"Sunrise: {datetime.fromtimestamp(sunrise)}")
                print(f"Sunset: {datetime.fromtimestamp(sunset)}")
                print(f"Date: {datetime.fromtimestamp(date)}")
                print(f"Timezone Offset (seconds): {timezone}")
                print("")



if __name__ == "__main__":
    print("Welcome to weather cli!")
    main()

    { 'visibility': 10000, 'wind': {'speed': 2.08, 'deg': 165, 'gust': 1.78}, 'clouds': {'all': 58}, 'dt': 1775136748, 'sys': {'country': 'IN', 'sunrise': 1775090338, 'sunset': 1775135196}, 'timezone': 19800, 'id': 1263364, 'name': 'Mathura', 'cod': 200}