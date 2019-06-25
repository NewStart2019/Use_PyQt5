#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import random

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont


def randomChar():
    '''
    随机生成chr
    :return:返回一个随机生成的chr
    '''
    return chr(random.randint(65, 120))


def randomBgColor():
    '''
    随机生成验证码的背景色
    :return:
    '''
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def randomTextColor():
    '''
    随机生成验证码的文字颜色
    :return:
    '''
    return (random.randint(32, 128), random.randint(32, 128), random.randint(32, 128))


w = 60 * 4
h = 60
# 创建一张图片，指定图片mode，长宽
image = Image.new('RGB', (w, h), (255, 255, 255))
# 设置字体类型及大小
font = ImageFont.truetype(font='arial.ttf', size=36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 遍历给图片的每个像素点着色
for x in range(w):
    for y in range(h):
        draw.point((x, y), fill=randomBgColor())

# 将随机生成的chr，draw如image
for t in range(4):
    draw.text((60 * t + 10, 10), randomChar(), font=font, fill=randomTextColor())

# 设置图片模糊
# image = image.filter(ImageFilter.BLUR)
# 保存图片
image.save('code.jpg', 'jpeg')