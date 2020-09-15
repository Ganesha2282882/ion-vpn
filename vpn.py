# Run me first. This is the Python script that runs the VPN.

import os
import requests as reqs
import re

message = "IonVPN -- Finally, a free VPN that sticks"
print(message)
print("Let's connect to a network.")
print("Lists of IP addresses:")
# IP List
print("Switzerland         :  2.16.92.0")
print("Japan               :  1.0.16.0")
print("Canada              :  2.57.168.0")
print("Germany             :  2.16.6.0")
print("United Kingdom      :  2.16.4.0")
print("Generic localhost   :  127.0.0.1")
print("Generic subnet mask :  255.255.255.0")
print("Generic server      :  0.0.0.0")
ip = input("What IP address do you want to choose?\n")
ua = input("What user agent string do you want to choose?\n")
sm = input("What \"sorry\" message do you want to choose?\n")
ad = input("What URL do you want to connect to and see?\n")
print("\n" * 100)
print(message)
print("Connecting to:", ad)
reqs.post(ad, data=sm, headers={"STATUS": "404", "HOST": ip}, allow_redirects=False)
wh = reqs.get(ad, headers={"STATUS": "404", "HOST": ip}, allow_redirects=False).text
wp = re.sub("<[^<]+>", "", str(wh))

print("Connection Complete!")
print("Here is the webpage:")
print(wp)
