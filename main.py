import requests
import json
import win32com.client as wincom

city = input("Enter the name of the city \n")
speak = wincom.Dispatch("SAPI.SpVoice")
url= f"http://api.weatherapi.com/v1/current.json?key=8e8138f4f37e40d4ad751252230207&q={city}"

r=requests.get(url)
print(r.text)

wdic = json.loads(r.text)
w=wdic["current"]["temp_c"]

text=f"The Current Weather of {city} is {w} degrees celsius "
speak.Speak(text)

