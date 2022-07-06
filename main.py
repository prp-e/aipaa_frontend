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
        self.token = ''