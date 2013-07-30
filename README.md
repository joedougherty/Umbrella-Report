# Umbrella Report

## 1.) Get an API key from Wunderground.com
http://www.wunderground.com/weather/api/d/login.html

## 2.) Set up your config file

### Example config file
    [weather]
    api_key = <insert key here>
    state = PA
    city = Philadelphia
    hour_cap = 12  

## 3.) Set up a cron job
    Email yourself the forecast every morning at 7am:

    Add a task to your crontab:
    0 07 * * * python ~/path/to/dir/getPrecip.py | mail -s "Umbrella Report" your.email@address
