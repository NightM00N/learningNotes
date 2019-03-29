import urllib
import requests
from xml.etree import ElementTree as ET

# 使用内置模块urllib发送HTTP请求，或者XML格式内容
"""
f = urllib.request.urlopen('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=424662508')
result = f.read().decode('utf-8')
"""


# 使用第三方模块requests发送HTTP请求，或者XML格式内容
r = requests.get('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=944879028')
result = r.text

# 解析XML格式内容
node = ET.XML(result)

# 获取内容
if node.text == "Y":
    print("在线")
else:
    print("离线")