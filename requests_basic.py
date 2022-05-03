#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests,json

def _req(URL="https://data.weather.gov.hk/weatherAPI/opendata/weather.php",payload= {'dataType': 'flw', 'lang': 'tc'}):
    response = requests.get(URL,params=payload).json()
    return response

if __name__ == '__main__':
    print(_req())
    
    
    
