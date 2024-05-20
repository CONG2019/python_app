#!/bin/python
# coding=utf-8

from urllib import request
from urllib.parse import unquote
from http import cookiejar
from time import sleep
from lxml import etree

cookie='''kt3F_b48a_saltkey=RScycs82; kt3F_b48a_lastvisit=1641663538; UM_distinctid=17e3cb3ea82de6-074fec8fb6bd288-336e464a-4f1a00-17e3cb3ea8389b; kt3F_b48a_st_p=64786%7C1641920343%7C8d92bb697e894694b266aecf86de55e2; kt3F_b48a_visitedfid=99D71D2D138; kt3F_b48a_viewid=tid_1955; kt3F_b48a_ulastactivity=451bqHH2upjUlO6OUIidlEEqjoPtk6pjEhg%2FcqcPKs9%2BQ9Cuz%2FVP; kt3F_b48a_auth=13efSsP8NZRcRQ0tx3ZWp7HC5wfx8UpnWbuaOXEqVmukXCfS5Lr8dPwvHf78BmLFhNf%2FS32i46rJ0O1BOb3mAqbJOw; kt3F_b48a_lastcheckfeed=64786%7C1641667456; kt3F_b48a_lip=203.168.1.204%2C1641919205; kt3F_b48a_smile=1D1; kt3F_b48a_st_t=64786%7C1641918277%7Cac2190e84540eab392271f6ad9328297; kt3F_b48a_forum_lastvisit=D_71_1641701172D_99_1641918277; CNZZDATA1279698056=556064220-1641657458-null%7C1641911282; kt3F_b48a_sid=k42PmN; kt3F_b48a_lastact=1641920344%09home.php%09spacecp; kt3F_b48a_noticeTitle=1; kt3F_b48a_sendmail=1'''
header={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'utf-8',
    'Referer':'http://www.shenbyj1.com/forum.php?mod=forumdisplay&fid=99&sortid=12&sortid=12&page=9'
    # 'Cookie':cookie
}
base_url="http://www.shenbyj1.com/"

def load_page(url):
    req = request.Request(url=url,headers=header,method='GET')
    try:
        rsp = request.urlopen(req)
    except BaseException:
        print("load: "+url+" fail!\n")
        return ""
    rsp_str=rsp.read().decode(encoding='utf-8')
    #print(rsp_str)
    return rsp_str

def get_mm_page_list(page_html):
    xpath="//*[@id=\"waterfall\"]/li/div/div/a/@href"
    page_tree=etree.HTML(page_html)
    mm_list=page_tree.xpath(xpath)
    return mm_list
    # print(mm_list)


if __name__ == "__main__":
    # base_url='http://www.shenbyj1.com/forum.php?mod=forumdisplay&fid=99&filter=sortid&orderby=dateline&sortid=12&page=3&t=3751933'
    # url='http://www.shenbyj1.com/forum.php?mod=viewthread&tid=3288&extra=page=3&filter=sortid&orderby=dateline&sortid=12&_dsign=68226271'
    for page in range(4,5):
        # url="http://www.shenbyj1.com/forum.php?mod=forumdisplay&fid=99&filter=sortid&orderby=dateline&sortid=12&page=%d"%page
        # url="http://www.shenbyj1.com/forum.php?mod=forumdisplay&fid=99&sortid=12&sortid=12&page=9"
        url = "http://www.shenbyj1.com/forum-99-4.html"
        page_html=load_page(url)
        if(page_html != ""):
            print("load page[%d] success."%page)
        else:
            print("load page[%d] fail."%page)
        mm_list=get_mm_page_list(page_html)
        for mm_page_url in mm_list:
            mm_page_full_url=base_url+mm_page_url
            mm_page_full_url=unquote(mm_page_full_url)
            print(mm_page_full_url)
            # mm_page_full_url="http://www.shenbyj1.com/forum.php?mod=viewthread&tid=3062&extra=page=3&filter=sortid&orderby=dateline&sortid=12"
            header['Referer']=mm_page_full_url
            mm_page = load_page(mm_page_full_url)
            print(mm_page)
            fd=open("tmp.html",'w')
            fd.write(mm_page)
            fd.close()
            break
    
# http://www.shenbyj1.com/forum.php?mod=viewthread&tid=3062&extra=page=3&filter=sortid&orderby=dateline&sortid=12&_dsign=a28b10d8
# http://www.shenbyj1.com/forum.php?mod=viewthread&tid=3421&extra=page=2&filter=sortid&orderby=dateline&sortid=12 