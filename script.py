#!/usr/bin/env python3
import requests
import urllib.request
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

#Create a new ToastNotifier object
obj = ToastNotifier()

#Process the data for the city of Zagreb
data = requests.get("https://www.timeanddate.com/weather/croatia/zagreb")
soup = BeautifulSoup(data.text, "html.parser")
temperature = str(soup.find_all("div", class_="h2"))

#Show the result using ToastNotifier
result = "The current temperature is " + temperature[17:22]
obj.show_toast("Weather update!", result, duration=10)