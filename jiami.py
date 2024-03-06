import base64
import requests
from lxml import etree

v = "vmess://ewogICJ2IjogIjIiLAogICJwcyI6ICJKUOiHquW7uuiKgueCuSIsCiAgImFkZCI6ICJkZW1vLmh1d28udG9wIiwKICAicG9ydCI6ICI0NDMiLAogICJpZCI6ICI3MUQwRjI1RS0xMEQ5LTZERDAtM0UwRi04ODUxODFGMjRBREQiLAogICJhaWQiOiAiMCIsCiAgInNjeSI6ICJhdXRvIiwKICAibmV0IjogIndzIiwKICAidHlwZSI6ICJub25lIiwKICAiaG9zdCI6ICIiLAogICJwYXRoIjogIi9odXdvMjA1MHRvcCIsCiAgInRscyI6ICJ0bHMiLAogICJzbmkiOiAiIiwKICAiYWxwbiI6ICIiLAogICJmcCI6ICIiCn0\n"

def ipQuery(ip):    
    url = "https://browserleaks.com/ip/" + ip
    req = requests.get(url).text
    html = etree.HTML(req)
    addr = html.xpath('//img[@class="flag-icon"]/@title')  #地址
    # print(addr)
    return addr[0].strip()

str = v+"\n"    
with open('jiedian.list', 'w') as f:
    with open('cf_ip.txt', 'r', encoding='utf-8') as f1:
        lines = f1.readlines()
        for l in lines:
            ip = l.strip()
            addr = ipQuery(ip)
            str = str + "vless://22a16011-ebdd-4af3-a317-3266fb70b091@"+ip+":443?encryption=none&security=tls&sni=cfpgvless.huwo.top&fp=randomized&type=ws&host=cfpgvless.huwo.top&path=%2F%3Fed%3D2048#"+addr+"\n"
              
        f.write(base64.b64encode(str.encode('utf-8')).decode('utf-8'))
