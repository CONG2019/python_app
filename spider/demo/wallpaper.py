#!/bin/python
# coding=utf-8

from urllib import request
from urllib.parse import unquote
from time import sleep
import requests
import json
import os
#from lxml import etree

img_tmp_url="/tmp/tmp.jpg"
change_wallpaper="feh --recursive --randomize --bg-fill "
# change_wallpaper="plasma-apply-wallpaperimage "
header={
    # 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'User-Agent':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'utf-8'
}

bizhi_vercel="https://bizhi.vercel.app/api/"
cnt=0
def bizhi_vercel_get_image():
    global cnt
    full_url="%s?cid=36&start=%d&count=1"%(bizhi_vercel,cnt)
    cnt = cnt + 1
    req = request.Request(url=full_url,headers=header,method='GET')
    try:
        rsp = request.urlopen(req)
    except BaseException:
        print("load: "+full_url+" fail!\n")
        return ""
    rsp_str=rsp.read().decode(encoding='utf-8')
    # print(rsp_str)
    data=json.loads(rsp_str)
    img_url=data['data'][0]['url_thumb']
    print("url=%s"%data['data'][0]['url_thumb'])
    return img_url

if __name__ == "__main__":
    while True:
        img_url=bizhi_vercel_get_image()
        try:
            print("download img...%s"%img_url)
            # request.urlretrieve(img_url, img_tmp_url)
            # download_cmd="curl %s -o %s%d.jpg"%(img_url, img_tmp_url,cnt)
            download_cmd="curl %s -o %s"%(img_url, img_tmp_url)
            os.system(download_cmd)
            print("downloaded")
        except BaseException:
            print("download image fail.")

        cmd="%s%s"%(change_wallpaper,img_tmp_url)
        os.system(cmd)
        sleep(60)

