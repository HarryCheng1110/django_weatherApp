from django.shortcuts import render
import json
import urllib.request

# Create your views here.
API_KEY = '4f526819847b8e90e06317f9d335f65b'

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, API_KEY)).read()
        json_data = json.loads(res)
        data = {'city': json_data['name'] + ', ' + json_data['sys']['country'],
                'coordinate': '(' + str(json_data['coord']['lon']) + ', ' + str(json_data['coord']['lat']) + ')',
                'weather': json_data['weather'][0]['main'],
                'temp': str(json_data['main']['temp'])+'k',
                'humidity': str(json_data['main']['humidity']),
                'windspeed': str(json_data['wind']['speed'])
        }
        
    else:
        data = {}

    return render(request, 'index.html', data)


