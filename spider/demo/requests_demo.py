#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import requests
import os

# rsp = requests.get("http://www.baidu.com/")
# print(rsp.status_code)
# print(rsp.content.decode("utf-8"))
# print(rsp.cookies)

# data = {
# 	'name':'germey',
# 	'age':22
# }
# r=requests.get("http://httpbin.org/get", params=data)
# print(r.text)

################################################################
# 正则表达式解析页面内容
# import re
# headers={
# 	'User-Agent':'Mzilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML,like Gecko)Chrome/52.0.2743.116 Safari/537.36'
# }
# r=requests.get("https://www.zhihu.com/explore",headers=headers)
# print(r.content.decode("utf-8"))
# pattern=re.compile('explore-feed.*question_link.*?(.*?)</a>',re.S)
# titles=re.findall(pattern,r.text)

################################################################
# 获取二进制数据
# r=requests.get("https://github.com/favicon.ico")
# with open('favicon.png
# ','wb') as f:
# 	f.write(r.content)

################################################################
# post请求
# data={'name':'germey','age':'22'}
# r=requests.post("http://httpbin.org/post",data=data)
# print(r.text)

################################################################
# 上传文件
# files={'file':open('favicon.png','rb')}

# r=requests.post("http://httpbin.org/post",files=files)
# print(r.text)

################################################################
# cookies
# import requests

# headers = {
#     'Cookie':'_zap=df4afa7d-2712-4c80-99c3-2b6c4ea4f7d7; d_c0=AIBXgYW-sBaPTgroYJSv2QLnwEK9HbPoFhU=|1682598226; YD00517437729195:WM_TID=+ZLrSNTVYRxAFUEEQQPRegc5+DTIiCwU; YD00517437729195:WM_NI=f6ZJ5XIE5J/pvQd8tSf1f0l0cBwJGgCJpXMcokHegOD+xObmLZBtlb/JJBX8biaXCQ81tg9w5pz0L7RavKJ+exhQqiHjPMGnXZHailUprm38h4ZIiz8FTic0B9+RQNEXRXo=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eeb2b86ff8f598a4f162fcb48aa7d15a838e9ab1d55cb6b6009bd952929a88d6aa2af0fea7c3b92aa6ea96abb8548b9bfbabae7cb68facd9f759a6efaad1ef3ca19eb9abc66d8196c0b9d069adb58886e64588f5b8b0e16790868e95ef6aed9686a3db34a2b7afb9c25bfcefbc88bc7df7b0b6d1cf3d92bfbaacc921a7a8a8b2f4638cb6a0aec6669c868882ec6897b0be8eb234acec96aaec72fc9a9c8ae23c82e7e5b3d44687889eb9ee37e2a3; __snaker__id=SR636B9o3iEPBpx7; q_c1=9974f3e8b3a4468f95495c066fbe043a|1683302764000|1683302764000; _xsrf=243b84b2-0ab2-40a6-84d6-f2ad0ac6771e; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1683970282,1685873479; z_c0=2|1:0|10:1686225923|4:z_c0|80:MS4xaXVQOUd3QUFBQUFtQUFBQVlBSlZUUzZ0WkdXYWJVZFMyTmoxRTl5NlpNRHVfT2hNUGpmTVd3PT0=|8f66845e1f267e156bd9a62bd6b55b557279bb199e44a52a49e5b6ebf370d2d6; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1686413392; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1686413497|1686413373',
#     'Host':'www.zhihu.com',
#     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
# }

# r = requests.get('https://www.zhihu.com', headers=headers)
# print(r.text)
# import requests
# cookies = '_zap=df4afa7d-2712-4c80-99c3-2b6c4ea4f7d7; d_c0=AIBXgYW-sBaPTgroYJSv2QLnwEK9HbPoFhU=|1682598226; YD00517437729195:WM_TID=+ZLrSNTVYRxAFUEEQQPRegc5+DTIiCwU; YD00517437729195:WM_NI=f6ZJ5XIE5J/pvQd8tSf1f0l0cBwJGgCJpXMcokHegOD+xObmLZBtlb/JJBX8biaXCQ81tg9w5pz0L7RavKJ+exhQqiHjPMGnXZHailUprm38h4ZIiz8FTic0B9+RQNEXRXo=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eeb2b86ff8f598a4f162fcb48aa7d15a838e9ab1d55cb6b6009bd952929a88d6aa2af0fea7c3b92aa6ea96abb8548b9bfbabae7cb68facd9f759a6efaad1ef3ca19eb9abc66d8196c0b9d069adb58886e64588f5b8b0e16790868e95ef6aed9686a3db34a2b7afb9c25bfcefbc88bc7df7b0b6d1cf3d92bfbaacc921a7a8a8b2f4638cb6a0aec6669c868882ec6897b0be8eb234acec96aaec72fc9a9c8ae23c82e7e5b3d44687889eb9ee37e2a3; __snaker__id=SR636B9o3iEPBpx7; q_c1=9974f3e8b3a4468f95495c066fbe043a|1683302764000|1683302764000; _xsrf=243b84b2-0ab2-40a6-84d6-f2ad0ac6771e; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1683970282,1685873479; z_c0=2|1:0|10:1686225923|4:z_c0|80:MS4xaXVQOUd3QUFBQUFtQUFBQVlBSlZUUzZ0WkdXYWJVZFMyTmoxRTl5NlpNRHVfT2hNUGpmTVd3PT0=|8f66845e1f267e156bd9a62bd6b55b557279bb199e44a52a49e5b6ebf370d2d6; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1686413392; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1686413497|1686413373'
# headers = {
#     'Host':'www.zhihu.com',
#     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
# }
# jar = requests.cookies.RequestsCookieJar()

# for cookie in cookies.split(';'):
#     key, value = cookie.split('=', 1)
#     jar.set(key,value)
    
# r = requests.get('https://www.zhihu.com', headers=headers)
# print(r.text)

################################################################
# 维持会话
# import requests
# s=requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r=s.get('http://httpbin.org/cookies')
# print(r.text)

################################################################
# 代理
# data = {
# 	'name':'germey',
# 	'age':22
# }
# proxies={
# 	"http":"112.250.107.37:53281",
# 	"https":"http://10.10.1.10:1080"
# }
# r=requests.get("http://httpbin.org/get",proxies=proxies, params=data)
# print(r.text)

################################################################
# 超时
# r=requests.get("https://www.taobaobao.com",timeout=1)
# print(r.status_code)

################################################################
# 身份认证
# import requests

# from requests.auth import HTTPBasicAuth
# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# # 更简单写法
# r =requests.get('http://localhost:5000,auth=('username','password'))

################################################################
# 准备请求
from requests import Request,Session

url='http://httpbin.org/post'
data={
	'name':'monkey'
}
headers={
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
s=Session()
req=Request('POST',url,data=data,headers=headers)
prepped=s.prepare_request(req)
r=s.send(prepped)
print(r.text)