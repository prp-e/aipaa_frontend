import librosa
import os
import pyaudio 
import requests
import soundfile as sf
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

    def play_sound(self, wave_file):
        x, _ = librosa.load(wave_file, sr=8000)
        sf.write(wave_file, x, 16000)

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
        headers = {'Authorization': f'Bearer {os.getenv("AIPAA_TOKEN")}'}
        payload = {'input_text': input_text}
        url = 'https://api.aipaa.ir/api/v1/voice/tts/'

        response = requests.post(url, headers=headers, data=payload)

        response = response.json()
        download_link = response['download_link']

        tts = requests.get(download_link, headers=headers)
        with open(file_name, 'wb') as f:
            f.write(tts.content)
        
        self.play_sound(file_name)
        os.remove(file_name)