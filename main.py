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
    