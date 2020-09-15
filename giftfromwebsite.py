# Web Browser for the VPN. Use this if you want to browse the web without encryption, or if you want to do some get requests.

import re
import requests as reqs
url = input("URL to open:\n")
pagept = reqs.get(url, allow_redirects=False).text
page = re.sub("<[^<]+>", "", pagept)
print(page) 
