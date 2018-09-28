"""
    Answer Processing class - calls a function then returns to request_processor
"""

from time import gmtime, strftime
import json
import requests


class AnswerProcessor:

    def __init__(self):
        pass

    @staticmethod
    def getTime():
        return "The time is: " + strftime("%H:%M:%S", gmtime())

    @staticmethod
    def getDate():
        return "Todays date is: " + strftime("%Y-%m-%d", gmtime())

    @staticmethod
    def getWeather():
        url = ('http://api.openweathermap.org/data/2.5/' +
               'weather?q=London,uk&appid=bf2af1e7a6110' +
               'd131268a1c3bdb9606f&units=metric')
        response = requests.get(url).text
        result = json.loads(response)
        return ("The weather today is: " + result['weather'][0]['description'] + " " +
                str(result['main']['temp']) + " C")

    @staticmethod
    def getLocation():
        url = 'http://api.ipstack.com/185.53.227.70?access_key=cf6acf373a6d8f4f5a52bd3301a482aa'
        response = requests.get(url).text
        result = json.loads(response)
        return "You are in " + result['city'] + ", in the " + result['country_name']

    @staticmethod
    def getName():
        url = 'http://localhost:8000/get_username/'
        response = requests.get(url).text
        result = json.loads(response)
        return "Your name is " + result[0]['username']
