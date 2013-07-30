import requests
import json
from ConfigParser import SafeConfigParser


parser = SafeConfigParser()
parser.read('') #point to config file

api_key = parser.get('weather', 'api_key')
state = parser.get('weather', 'state')  #two-letter state abbreviation
city = parser.get('weather', 'city')    
hour_cap = parser.get('weather', 'hour_cap')

target = 'http://api.wunderground.com/api/'+ api_key +'/hourly/q/'+ state +'/'+ city +'.json'

weather = requests.get(target)

if weather.status_code == 200:
    parsed_json = json.loads(weather.text)
    hours_reported = 0   

    for hours in parsed_json['hourly_forecast']:
        if hours_reported < hour_cap:
            time = hours['FCTTIME']['civil'].strip()
            temp = hours['temp']['english'].strip()
            chance = hours['pop'].strip()

            print(time + '\n' + temp  + 'F' + '  ' + chance + '%' + '\n')

            hours_reported = hours_reported + 1
