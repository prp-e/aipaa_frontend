from datetime import datetime
import os
import pyaudio 
import requests
import ssl
import urllib.parse
import wave

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


class AipaaFrontend:
    def __init__(self):
        pass

    def play_sound(self, wave_file):
        wave_file = wave.open(wave_file, 'rb')
        chunk = 1024
        player = pyaudio.PyAudio() 

        stream = player.open(
            format = player.get_format_from_width(wave_file.getsampwidth()),
            channels = wave_file.getnchannels(), 
            rate = wave_file.getframerate(),
            output = True
        )

        data = wave_file.readframes(chunk) 

        while data != b'':
            stream.write(data)
            data = wave_file.readframes(chunk)
        
        stream.close()
        player.terminate()
    
    def say(self, input_text, file_name='tts.wav', keep_file=False):
        input_text = urllib.parse.quote(input_text)
        headers = {'Authorization': f'Bearer {os.getenv("AIPAA_TOKEN")}', 'content-type': 'multipart/form-data'}
        payload = f'input_text={input_text}'
        url = 'https://api.aipaa.ir/api/v1/voice/tts/'

        response = requests.post(url, headers=headers, data=payload)

        return response.text, response.status_code
