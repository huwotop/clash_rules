from fofa_hack import fofa
import requests
from lxml import etree

def ipQuery(ip):    
    url = "https://browserleaks.com/ip/" + ip
    req = requests.get(url).text
    html = etree.HTML(req)
    addr = html.xpath('//img[@class="flag-icon"]/@title')  #地址
    # print(addr)
    return addr[0].strip()

def main():
    result_generator = fofa.api('server=="cloudflare" && port=="80" && header="Forbidden" && country=="CN"', endcount=100)
    with open('jiedian.txt', 'w') as f:
        for data in result_generator:
            for d in data:
                ip = (d.split('//'))[1].strip()
                addr = ipQuery(ip)
                f.write("vless://22a16011-ebdd-4af3-a317-3266fb70b091@"+ip+":443?encryption=none&security=tls&sni=cfpgvless.huwo.top&fp=randomized&type=ws&host=cfpgvless.huwo.top&path=%2F%3Fed%3D2048#"+addr+"\n")

if __name__ == '__main__':
    main()