# 获取默认的规则

import requests

# 直链网址
url01 = "https://github.com/LM-Firefly/Rules/blob/master/CCC-Global.list"  #全球常见 云计算公司
url02 = "https://github.com/LM-Firefly/Rules/blob/master/CCC-CN.list" #中国常见 云计算公司
url03 = "https://github.com/LM-Firefly/Rules/blob/master/Special/Local-LAN.list" #局域网 IP 段
url04 = "https://github.com/LM-Firefly/Rules/blob/master/Special/LAN-Special-Apps.list" #局域网特殊应用域名（投屏、广播 等）
url05 = "https://github.com/LM-Firefly/Rules/blob/master/Special/DMCA-Sensitive.list" #DMCA 敏感域名（主要针对机场审计 tracker、迅雷）
url06 = "https://github.com/LM-Firefly/Rules/blob/master/Special/Video-Crack.list" #盗版视频解析站
url07 = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Microsoft.list" #微软服务
url08 = "https://github.com/LM-Firefly/Rules/blob/master/Special/DNS.list" #常用 DNS
url09 = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/LocalAreaNetwork.list"
url010 = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/UnBan.list"
url011 = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Apple.list"
url012 = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaDomain.list"
url013 = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaMedia.list"
url014 = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaCompanyIp.list"
url015 = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaIp.list"


# 拦截网址
url11 = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list"
url12 = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list"

directUrls = [url01,url02,url03,url04,url05,url06,url07,url08,url09,url010,url011,url012,url013,url014,url015]
rejectUrls = [url11,url12]

# 写入文件
with open("direct.txt","w",encoding="utf-8") as f:
    with open("exSite.txt","r",encoding="utf-8") as f1:
        f.write(f1.read())
        f.write("\n")
        for url in directUrls:
            html = requests.get(url).text
            f.write(html+"\n")

with open("reject.txt","w",encoding="utf-8") as f:
    for url in rejectUrls:
        html = requests.get(url).text
        f.write(html+"\n")
