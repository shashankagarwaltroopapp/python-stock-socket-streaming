"""
    Created on Monday Feb 2 2022

    @author: Nishant Jain

    :copyright: (c) 2022 by Angel One Limited
"""

from SmartWebSocketV2 import SmartWebSocketV2
import os
from dotenv import load_dotenv
from readStockTokensFromDatabase import readStockTokensFromDatabase


stockTokenList = readStockTokensFromDatabase()

# SMARTAPI_JWT="eyJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6IkE5NTgwMTUiLCJyb2xlcyI6MCwidXNlcnR5cGUiOiJVU0VSIiwidG9rZW4iOiJleUpoYkdjaU9pSklVelV4TWlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKemRXSWlPaUpCT1RVNE1ERTFJaXdpWlhod0lqb3hOams1TURBME9EYzBMQ0pwWVhRaU9qRTJPVGc1TURjME56WXNJbXAwYVNJNklqRTNNMk0zTlRjMkxXTTRaR1l0TkRGa09DMDVZV015TFdNNU5UQXdPRE00WW1ZNE5DSXNJbTl0Ym1WdFlXNWhaMlZ5YVdRaU9qWXNJbk52ZFhKalpXbGtJam9pTXlJc0luVnpaWEpmZEhsd1pTSTZJbU5zYVdWdWRDSXNJblJ2YTJWdVgzUjVjR1VpT2lKMGNtRmtaVjloWTJObGMzTmZkRzlyWlc0aUxDSm5iVjlwWkNJNk5pd2ljMjkxY21ObElqb2lNeUo5LjBHckI4VlRHemIzb3ltYloxZi1qSlgyMmxkLXUwQWFlLUNUTnpfV1N3bmdJR0xpejdDWGVlVmYzUlRGOTVGZFJBOUt0Q1NLNXVsSXhfOEVLRUFGeEJBIiwiQVBJLUtFWSI6InRLRGFKcVNOIiwiaWF0IjoxNjk4OTA3NTM2LCJleHAiOjE2OTkwMDQ4NzR9.uKGMPNdmtC3HDZlZRsVGCr1xoAvXjRYwecuxkuR5zV2PSE1ZSojAbH810-xp2kYQU9vGqRHiSgzZMaLrGm2FuQ"
# SMARTAPI_REFRESH_TOKEN="eyJhbGciOiJIUzUxMiJ9.eyJ0b2tlbiI6IlJFRlJFU0gtVE9LRU4iLCJSRUZSRVNILVRPS0VOIjoiZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnpkV0lpT2lKQk9UVTRNREUxSWl3aVpYaHdJam94TmprNE9UVXdOek0yTENKcFlYUWlPakUyT1RnNU1EYzBOellzSW1wMGFTSTZJakV4WkdZeFl6aGlMV05pWlRndE5ERmxaUzFpWXpNMUxUVXdZemRtWkRFMU1tTmhOeUlzSW5SdmEyVnVJam9pVWtWR1VrVlRTQzFVVDB0RlRpSXNJblZ6WlhKZmRIbHdaU0k2SW1Oc2FXVnVkQ0lzSW5SdmEyVnVYM1I1Y0dVaU9pSjBjbUZrWlY5eVpXWnlaWE5vWDNSdmEyVnVJbjAudWhDSzhleE9MVDdQdGcyY29GcWd6cGVKS2Jsbjh4Si1sZXVqenhVVnQ3N2JmNGFZa1M0N0J2Rk9kUVg1Rkw1OTQ4c0hvWFhxSTU4WHhMeUc3UHZmbXciLCJpYXQiOjE2OTg5MDc1MzZ9.wmcVCE2yubbljLur6yoC6LdbiW7HZOv_ReTO1pC8zbY6B0giGqzoehiX4OiIKjqTM4Pv6jESxv1_Skc5qwbDRg"
# SMARTAPI_FEED_TOKEN ="eyJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6IkE5NTgwMTUiLCJpYXQiOjE2OTg5MDc1MzYsImV4cCI6MTY5ODk5MzkzNn0.SR2eTIwJ6uiOp0XphFVqMXUWHQ4PiNs6lpmtPfQ2BkMA5OUHc1OGDK4PxneZVHAKuO5DFRVsIKZOYzmqxCv0fw"
# SMARTAPI_API_KEY="tKDaJqSN"
# SMARTAPI_CLIENT_CODE="A958015"
# SMARTAPI_CLIENT_PASSWORD="2437"

AUTH_TOKEN = 'Bearer ' + os.environ["SMARTAPI_JWT"]
API_KEY = os.environ["SMARTAPI_API_KEY"]
CLIENT_CODE = os.environ["SMARTAPI_CLIENT_CODE"]
FEED_TOKEN = os.environ["SMARTAPI_FEED_TOKEN"]

# AUTH_TOKEN = 'Bearer ' + SMARTAPI_JWT
# API_KEY = SMARTAPI_API_KEY
# CLIENT_CODE = SMARTAPI_CLIENT_CODE
# FEED_TOKEN = SMARTAPI_FEED_TOKEN

correlation_id = "abcde"
action = 1
mode = 1

token_list = [{"exchangeType": 1, "tokens": stockTokenList}]

sws = SmartWebSocketV2(AUTH_TOKEN, API_KEY, CLIENT_CODE, FEED_TOKEN)


def on_data(wsapp, message):
    print("Ticks: {}".format(message))


def on_open(wsapp):
    print("on open")
    sws.subscribe(correlation_id, mode, token_list)


def on_error(wsapp, error):
    print(error)


def on_close(wsapp):
    print("Close")


# Assign the callbacks.
sws.on_open = on_open
sws.on_data = on_data
sws.on_error = on_error
sws.on_close = on_close

sws.connect()