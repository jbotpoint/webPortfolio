import pip._vendor.requests as rq

from package import keys

def getWeather(city):
    base_url = "http://api.weatherapi.com/v1/current.json" + "?key=" + kList[0] + "&q=" + city
    response = rq.get(base_url)
    if response.status_code == rq.codes.ok:
        responseJson = response.json()
        return responseJson

    return False
