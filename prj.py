import requests

key = "a9321d7bbc24451a2439057b8fdce3b9"
city = "New York"

res = requests.get("https://api.openweathermap.org/data/2.5/weather", params={"q": city, "units" : "metric", "lang" : "RU", "APPID": key})
data = res.json()
print("Город: ", city)
print("Погодные условия: ", data['main']['temp'])
print("Температура: ", data["main"]["temp"])
print("Мин.температура: ", data["main"]["temp_min"])
print("Макс.температура : ", data["main"]["temp_max"])