import requests
import random
from sys import exit

url = "http://www.reddit.com/r/todayilearned/new/.json"
headers = {'User-Agent':'windows:test.py:v0.1 (by /u/shashwat986)'}
r = requests.get(url, headers = headers)

if r.status_code != 200:
	print ("There seems to be a problem: " + str(r.status_code))
	exit(0)

d = r.json()

TILs = []
for element in d["data"]["children"]:
	TILs.append(element["data"]["title"])

print random.choice(TILs)