#!/bin/python
# coding=utf-8

from urllib import request
from urllib.parse import unquote
from http import cookiejar
from time import sleep
from lxml import etree

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image

pdfmetrics.registerFont(TTFont('SimSun', 'SIMSUN.ttf'))
styles = getSampleStyleSheet()
TITLE = styles['Title']
TITLE.fontSize = 54
TITLE.leading = 58
BODY = styles['Normal']
BODY.fontSize = 30
BODY.leading = 34
TITLE.fontName = 'SimSun'
BODY.fontName = 'SimSun'

# base_url = "http://www.shenbyj1.com/forum.php?mod=forumdisplay&fid=99"
# base_url = "http://www.shenbyj1.com/forum.php?mod=forumdisplay&fid=99&sortid=12&sortid=12&page=13" #gz
# base_url = "http://www.shenbyj1.com/forum-97-6.html" #sz
base_url = "http://www.shenbyj1.com/forum-100-1.html"   #fgh
page_num=1
MAX_WAIT_TIME = 180
SAVE_PATH="data1/"
IMG_PATH='imgs/'
if __name__ == "__main__":
    br = webdriver.Chrome()
    br.get(base_url)
    try:
        WebDriverWait(br, MAX_WAIT_TIME)
    except BaseException:
        print("wait main page tiemout, continue")
    print("load main finsh")
    sleep(60)
    cnt = 1
    imgs_cnt = 1
    while(True):
        mm_lists = br.find_elements_by_xpath("//*[@id=\"waterfall\"]/li/div/div/a")
        main_win=br.current_window_handle
        # print(br.find_elements_by_xpath("//*[@id=\"waterfall\"]/li/div/div/a"))
        for i in range(len(mm_lists)):
            print("page:%d"%page_num)
            mm_page=mm_lists[i]
            mm_page_html=mm_page.get_attribute("href")
            print(mm_page_html)
            newwindow = "window.open(\"%s\")"%mm_page_html
            br.execute_script(newwindow)
            br.switch_to.window(br.window_handles[1])
            try:
                WebDriverWait(br, MAX_WAIT_TIME)
            except BaseException:
                print("wait mm page tiemout, continue")
                # continue
            sleep(8)
            # get message and save to pdf
            try:
                # msg_title_lists = br.find_elements_by_xpath("//*/tbody/tr[1]/td/div[2]/div/div/font/fieldset/li/b")
                title = br.find_element_by_xpath("//*[@id=\"postlist\"]/div[1]/h1")
                print("finsh title")
                msg_lists = br.find_elements_by_xpath("//*/tbody/tr[1]/td/div[2]/div/div/font/fieldset/li")
                print("finsh, msg_list")
                wchat = br.find_element_by_xpath("//*/tbody/tr[1]/td/div[2]/div/div/font/fieldset/p/span")
                print("finsh wchat")
                imgs = br.find_elements_by_xpath("//*/ignore_js_op/dl/dd/div/img")
                print("finsh imgs")
                main_img = br.find_element_by_xpath("//*/tbody/tr[1]/td/div[2]/font/font/font/font/div[1]/div/dl/dd/div[2]/img")
            except BaseException:
                print("can not get mm message!")
                br.close()
                br.switch_to.window(br.window_handles[0])
                continue
            # print(msg_title_lists)

            # save message
            file_name=SAVE_PATH+"%d.pdf"%cnt
            cnt = cnt + 1
            doc = SimpleDocTemplate(file_name)
            doc.pagesize = (2048, 1280*6)
            story = []
            story.append(Paragraph(title.text, TITLE))
            print(title.text)
            for i in range(len(msg_lists)):
                story.append(Paragraph(msg_lists[i].text, BODY))
                print(msg_lists[i].text)
            print(wchat.text)
            story.append(Paragraph(wchat.text, BODY))

            img_url = main_img.get_attribute("src")
            print(img_url)
            img_path = "imgs/%d.jpeg"%imgs_cnt
            imgs_cnt = imgs_cnt + 1
            try:
                request.urlretrieve(img_url, img_path)
                IMG = Image(img_path)
                story.append(IMG)
            except BaseException:
                print("download image fail.")
            for i in range(len(imgs)):
                img_url = imgs[i].get_attribute("src")
                print(img_url)
                img_path = "imgs/%d.jpeg"%imgs_cnt
                imgs_cnt = imgs_cnt + 1
                try:
                    request.urlretrieve(img_url, img_path)
                    IMG = Image(img_path)
                    story.append(IMG)
                except BaseException:
                    print("download image fail.")
                    continue


            try:
                text_lists = br.find_element_by_xpath("//*/tbody/tr[1]/td/div[2]/div/div[1]/table/tbody/tr/td")
                for i in range(len(text_lists)):
                    story.append(Paragraph(text_lists[i].text, BODY))
            except BaseException:
                print("get text fail.")
            doc.build(story)
            br.close()
            br.switch_to.window(br.window_handles[0])
        # break
        # next_page=br.find_element_by_xpath("//*[@id=\"fd_page_bottom\"]/div/a[11]")
        # next_page.click()
        page_num = page_num + 1
        next_page_url = "http://www.shenbyj1.com/forum-100-%d.html"%page_num
        # br = webdriver.Chrome()
        print("next page:%s"%next_page_url)
        br.get(next_page_url)
        try:
            WebDriverWait(br, MAX_WAIT_TIME)
        except BaseException:
            print("wait next page tiemout, continue")
            continue
    sleep(100)