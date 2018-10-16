# function to get weather response
import requests
def weather_response(location, API_key):
    
    url = 'http://api.openweathermap.org/data/2.5/forecast?q='+location+'&appid='+API_key+'&units=metric'
    res = requests.get(url)
    data = res.json()
    return data


# function to check for valid response 
def has_error(location,json):
    if data['cod'] == "404":
        print("error")
    else:
        day=0
        temp = data['list'][day]['main']['temp']
        print(temp)

    return 

# function to get attributes on nth day
def get_temperature (json, n=0):
    temp = data['list'][n]['main']['temp']
    return temp

def get_humidity(json, n=0):
    humidity=data['list'][n]['main']['humidity']
    return humidity

def get_pressure(json, n=0):
    pressure=data['list'][n]['main']['pressure']
    return pressure

def get_wind(json, n=0):
    wind=data['list'][n]['wind']['speed']
    return wind

def get_sealevel(json, n=0):
    sealevel = data['list'][n]['main']['sea_level']
    return sealevel

if __name__=='__main__':
    API_key = "Your API Key"
    location = "Delhi"
    data=weather_response(location,API_key)
    T=get_temperature(data)
    H=get_humidity(data)
    P=get_pressure(data)
    W=get_wind(data)
    S=get_sealevel(data)
    print "Temparature is ",T 
    print "Humidity is ",H
    print "Pressure is ",P
    print "Wind Speed is ",W
    print "Sealevel is ",S
    
