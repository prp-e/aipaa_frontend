import os
from playsound import playsound
import requests
import ssl
import wave
import warnings
warnings.filterwarnings('ignore')

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


class AipaaFrontend:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = ''
    
    def authenticate(self):
        url = "https://api.aipaa.ir/auth/token"
        payload = {"client_id": self.client_id, "client_secret": self.client_secret, "grant_type": "client_credentials", "scope": "file_manager text voice image video"}
        request = requests.post(url, data=payload)

        self.token = request.json()['access_token']
        return self.token
    
    def tts(self, text):
        url = "https://api.aipaa.ir/api/v1/voice/tts"
        payload = {"input_text": text}
        headers = {'Authorization': 'Bearer ' + self.token}
        request = requests.post(url, data=payload, headers=headers)

        return request.text
    