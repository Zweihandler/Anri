#!/usr/bin/env python3



from typing import Text
from datetime import datetime

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:



    while True:

        audio = r.listen(source)

        Text = r.recognize_google(audio)
    
        if str(Text).lower() == 'time': #kata kunci untuk menampilkan date time

            now = datetime.now() 
            year = now.strftime("%Y")
            print("year:", year)

            month = now.strftime("%m")
            print("month:", month)

            day = now.strftime("%d")
            print("day:", day)

            time = now.strftime("%H:%M:%S")
            print("time:", time)

            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            print("date and time:",date_time)

            dy = now.strftime("%a")
            print("Today :",dy)
        break


