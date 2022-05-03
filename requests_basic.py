#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests,json

#1
#Extract data from URL using HTTP GET method.
#Example Used from HKO:https://www.hko.gov.hk/tc/weatherAPI/doc/files/HKO_Open_Data_API_Documentation_tc.pdf
def _req(URL="https://data.weather.gov.hk/weatherAPI/opendata/weather.php",payload= {'dataType': 'flw', 'lang': 'tc'}):
    response = requests.get(URL,params=payload).json()
    return response

#2
#A light weight method to check validity of a request. Code 200 is all good. Code 401 usually means your authentication process failed.
def _req_code(URL="https://data.weather.gov.hk/weatherAPI/opendata/weather.php",payload= {'dataType': 'flw', 'lang': 'tc'}):
    status_code = requests.get(URL,params=payload).status_code
    return status_code

if __name__ == '__main__':
    print(_req()) #1
    print(_req_code()) #2
    
    
    
    
  
    
    
    
