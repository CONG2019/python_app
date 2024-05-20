#!/usr/bin/python3.11
# -*- coding: utf-8 -*-
import jieba
from wordcloud import WordCloud

# 字体 fc-list
# /usr/share/fonts/truetype/hack/Hack-Regular.ttf
# /usr/share/fonts/truetype/wqy/wqy-microhei.ttc

txt='被萧炎这突如其来的厉喝声吓了一跳兰芝傻傻的望着前者脑袋忽然有些转不过弯来这…这小家伙竟然敢这般吼自己？'
words=jieba.lcut(txt)
newtxt=' '.join(words)
print(newtxt)
wc=WordCloud(font_path='/usr/share/fonts/truetype/wqy/wqy-microhei.ttc')
wc.generate(newtxt)
wc.to_file('tmp.jpg')

# 带背景图云
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

mask = np.array(Image.open("face.jpg"))
wc = WordCloud(background_color="white",\
                      width = 800,\
                      height = 600,\
                      max_words = 200,\
                      max_font_size = 80,\
                      mask = mask,\
                      contour_width = 3,\
                      contour_color = 'steelblue',\
                      font_path='/usr/share/fonts/truetype/wqy/wqy-microhei.ttc'
                      ).generate(newtxt)
wc.to_file('face_wordcloud.jpg')
