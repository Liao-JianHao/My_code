import urllib.request
import urllib.parse
import json
"""
有道有反爬机制
秘钥：Cookie
"""

# 旧地址
content = input("请输入需要翻译的内容：")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartesult=rule&ssmartresul=ugc&sessionFrom=http://www.youdao.com/"
data = {}
data["i"] = content
data["from"] = "AUTO"
data["to"] = "AUTO"
data["smartresult"] = "dict"
data["client"] =  "fanyideskweb"
data["salt"] =  "15523896764982"
data["doctype"] = "json"
data["version"] = "2.1"
data["keyfrom"] = "fanyi.web"
data["action"] = "FY_BY_REALTlME"
data["typoResult"] = "false"

data = urllib.parse.urlencode(data).encode("utf-8")  #parse 解析数据进行编码
response = urllib.request.urlopen(url, data)  # 地址和格式数据
html = response.read().decode("utf-8")  # 将响应的数据进行解码
target = json.loads(html)  # 轻量级，将已编码的 JSON 字符串解码为 Python 对象
print(f"翻译的结果是：{target['translateResult'][0][0]['tgt']}")