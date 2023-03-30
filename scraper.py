import os
from time import sleep
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
to_location = 'MIA'
url = "https://www.kayak.com/flights/NYC-{to_location}/2023-04-20/2023-04-30?sort=bestflight_a".format(
    to_location=to_location)
