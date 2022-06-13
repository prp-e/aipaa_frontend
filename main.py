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
    def __init__(self):
        pass

    def say(self, input_text, file_name='tts.wav', keep_file=False):
        headers = {'Authorization': f'Bearer {os.getenv("AIPAA_TOKEN")}'}
        payload = {'input_text': input_text}
        url = 'https://api.aipaa.ir/api/v1/voice/tts/'

        response = requests.post(url, headers=headers, data=payload)

        response = response.json()
        download_link = response['download_link']

        tts = requests.get(download_link, headers=headers)
        with open(file_name, 'wb') as f:
            f.write(tts.content)
        
        playsound(file_name)
        os.remove(file_name)