#!/usr/bin/python3

import urllib.request

response=urllib.request.urlopen('https://www.github.com')
#print(response.read().decode('utf-8'))
print(response.read())
print(response.getheaders())
