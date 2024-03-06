import base64
import requests
from lxml import etree

def ipQuery(ip):    
    url = "https://browserleaks.com/ip/" + ip
    req = requests.get(url).text
    html = etree.HTML(req)
    addr = html.xpath('//img[@class="flag-icon"]/@title')  #地址
    # print(addr)
    return addr[0].strip()

with open('cf_ip.txt', 'r') as f:
    lines = f.readlines()

with open('jiedian.txt', 'w', encoding='utf-8') as f:
    f.write("vmess://ewogICJ2IjogIjIiLAogICJwcyI6ICJKUOiHquW7uuiKgueCuSIsCiAgImFkZCI6ICJkZW1vLmh1d28udG9wIiwKICAicG9ydCI6ICI0NDMiLAogICJpZCI6ICI3MUQwRjI1RS0xMEQ5LTZERDAtM0UwRi04ODUxODFGMjRBREQiLAogICJhaWQiOiAiMCIsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6ICJub25lIiwKICAiaG9zdCI6ICIiLAogICJwYXRoIjogIi9odXdvMjA1MHRvcCIsCiAgInRscyI6ICJ0bHMiLAogICJzbmkiOiAiIiwKICAiYWxwbiI6ICIiLAogICJmcCI6ICIiCn0\n")
    for line in lines:
        str = line.strip()
        f.write("vless://22a16011-ebdd-4af3-a317-3266fb70b091@"+str+":443?encryption=none&security=tls&sni=cfpgvless.huwo.top&fp=randomized&type=ws&host=cfpgvless.huwo.top&path=%2F%3Fed%3D2048#"+ipQuery(str)+"\n")

with open('jiedian.txt', 'r', encoding='utf-8') as f:
    with open('jiedian.md', 'w') as f2:
        str = f.read()
        f2.write(base64.b64encode(str.encode('utf-8')).decode('utf-8'))
