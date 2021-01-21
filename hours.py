# Hello Biden&Harris / Goodbye Trump countdown!
# Calculate hours / mins until 9am PST 
import os
import time
import datetime
from dateutil.relativedelta import relativedelta
import urllib.request 

# get LED server address
led_server = os.environ['LED_SERVER']
if led_server:
    print("LED SERVER is " + led_server)
else:
    print("Missing LED_SERVER env variable")

starttime = time.time()
while True:
    print("tick")
    rd = relativedelta(datetime.datetime(2021,1,20, 9, 0, 0), datetime.datetime.now())

    if rd.minutes == 1:
        minstring = "+minute..."
    else:
        minstring = "+minutes..."
    if rd.hours == 1:
        hourstring = "+hour,+"
    else:
        hourstring = "+hours,+"
    print (str(rd.hours) + hourstring + str(rd.minutes) + minstring)

    url = led_server + "/text?t=" + str(rd.hours) + hourstring + str(rd.minutes) + minstring 
    print(url);
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(html)
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))




