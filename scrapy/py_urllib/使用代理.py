import urllib.request
import random


url = "http://www.whatismyip.com.tw/"
print("添加代理IP地址(IP:端口号),多个IP地址用英文的分号隔开！")
iplist = input("请开始输入：").split(sep=";")
while True:
    ip = random.choice(iplist)
    proxy_support = urllib.request.ProxyHandler({"http":ip})
    opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)
# response = urllib.request.urlopen(url)
# html = response.read().decode("utf-8")
# print(html)