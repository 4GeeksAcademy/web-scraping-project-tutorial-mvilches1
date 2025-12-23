import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

sitio = requests.get('https://en.wikipedia.org/wiki/List_of_Spotify_streaming_records')
