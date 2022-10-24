import requests

city = ["Moscow","Saint-Petersburg","Novgorod", "Lipetsk"]
for i in city:
    link = f"https://wttr.in/{i}"
    response = requests.get(link, params="1MQ&lang=ru")
    print(response.text)