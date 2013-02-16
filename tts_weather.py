#
# Scrape weather of Chennai and convert it to speech
#
import requests
import subprocess
from BeautifulSoup import BeautifulStoneSoup

audio_file = 'test.mp3'
weather_url = "http://weather.yahooapis.com/forecastrss?w=2295424&u=c"
tts_api = "http://tts-api.com"

try:
    res = requests.get(weather_url)
    soup = BeautifulStoneSoup(res.content)
    conditions = soup.find('yweather:condition').attrs
    temperature = [value for (key, value) in conditions if key == "temp"][0]
    tts_url = ''.join([tts_api, '/tts.mp3?q=The_weather_in_chennai_is_', temperature, '_degree_centigrade'])
    response = requests.get(tts_url)
    file = open(audio_file, 'w')
    file.write(response.content)
    file.close()
    res = subprocess.call(['mplayer', '-really-quiet', audio_file])
except Exception, e:
    print e
