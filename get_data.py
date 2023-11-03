import requests
import json
from requests import post, get
from datetime import datetime

token = "........................"
access_token =token
def get_recently_played(new_token, start_date):
    limit = 50
    timestamp_ms = int(start_date.timestamp())* 1000
    user_id ="317rj6elz2onmjsrhtju5ov5ssea"
    url = "https://api.spotify.com/v1/me/player/recently-played"
#   url = f"https://api.spotify.com/v1/users/{user_id}/player/recently-played"
    endpoint = f"{url}?limit={limit}&before={timestamp_ms}"

    headers ={
        "Authorization": f"Bearer {new_token}"
    }

    result = requests.get(endpoint, headers=headers)

    data = result.json()
    return data


start_date = datetime.datetime(2023, 10, 14)
recently_played = get_recently_played(access_token, start_date)
print(recently_played)

