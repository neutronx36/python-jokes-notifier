import requests
from plyer import notification
from time import sleep

while True:
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': 'eLlayU1UTHHkGaJFcJuckw==x48IQgvhIbv3c5ON'})
    if response.status_code == 200:
        data = response.json()
        joke = data[0]['joke']
        notification.notify("Daily Jokes",joke,app_icon = "joke.ico")
        sleep(7200)
   