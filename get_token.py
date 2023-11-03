from dotenv import load_dotenv
import os
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 
import spotipy.util as util
sp = spotipy.Spotify() 
import requests
import base64
from spotipy.oauth2 import SpotifyOAuth
import json
from requests import post, get
from datetime import datetime
import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import datetime
import sqlite3
import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3


#-----------------------------------------------------------------------------------------------------
#Take environment variables from .env file and scope
load_dotenv()  
client_id = os.getenv("Client_ID")
client_secret = os.getenv("Client_secret")
redirect_uri= os.getenv("redirect_uri")
scope = "user-read-recently-played"


#-----------------------------------------------------------------------------------------------------
#Request User Authorization
auth_code = requests.get('https://accounts.spotify.com/authorize', {
    'client_id': client_id,
    'response_type': 'code',
    'redirect_uri': 'uri',
    'scope': scope
})
print(auth_code)


#-----------------------------------------------------------------------------------------------------
#Get Authentication Token 
def get_token():
    url = 'https://accounts.spotify.com/api/token'
    data  = {
        'grant_type':"client_credentials",        
        'code' : "code",
        "scope": scope,
        'redirect_uri' : redirect_uri
        } 
    encoded = base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii")
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + encoded
    }


#Call requests library to make a request to server
    token = requests.post(url,data=data, headers=headers)
    return token.text
print(get_token())


#-----------------------------------------------------------------------------------------------------
#Get "access_token" from get_token() with JSON
#Parse the JSON and convert it into a Python Dictionary, get "access_token" and check if that exists in the JSON response
response_data = json.loads(get_token())
access_token = response_data.get("access_token")
print(access_token)
if access_token:
    print("Access Token:", access_token)
else:
    print("Access Token not found in the JSON response")


#-----------------------------------------------------------------------------------------------------
#Access Token-Create the string, which contains the credentials and permissions
def get_auth_header(access_token):
    auth_token = {"Authorization": "Bearer "+ access_token}
    return auth_token
print(get_auth_header(access_token))
token = get_auth_header(access_token)
