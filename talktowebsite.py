# Talk to a website. Hack a website. You can do anything.

import requests as reqs

message, url = input("What do you want to send?\n"), input("Who do you want to send the message?\n")
reqs.post(url, data=message)
