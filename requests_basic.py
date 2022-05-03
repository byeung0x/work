#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests,json

#Example Used from HKO:https://www.hko.gov.hk/tc/weatherAPI/doc/files/HKO_Open_Data_API_Documentation_tc.pdf
def _req(URL="https://data.weather.gov.hk/weatherAPI/opendata/weather.php",payload= {'dataType': 'flw', 'lang': 'tc'}):
    response = requests.get(URL,params=payload).json()
    return response

if __name__ == '__main__':
    print(_req())
    
    
    
