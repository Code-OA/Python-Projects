from config import API_KEY
import requests

def get_weather(city):
    try:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")

        status = response.status_code
        data = response.json()

        if( status == 200):
            return {"data" : data , "err": None}
        elif status == 404:
            return {"data" : None , "err": "Not found!"}
        elif status == 401:
            return {"data" : None , "err": "Unauthorised access denied!"}
    except requests.exceptions.ConnectionError as e:
        return {"data" : None , "err": "No internet connection!"}
    except requests.exceptions.Timeout as t:
        return {"data" : None , "err": "Couldn't fetch! Even after too many requests!"}

   