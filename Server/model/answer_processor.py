"""
    Answer Processing class - calls a function then returns to request_processor
"""

from time import gmtime, strftime

import json
import requests
class AnswerProcessor:

    @staticmethod
    def getTime():
        return "The time is: " + strftime("%H:%M:%S", gmtime())

    @staticmethod
    def getName():
        return 0

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



