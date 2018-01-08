# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 08:18:09 2018

@author: ava
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
if __name__ == '__main__':
    #show image with imshow
    img = cv2.imread('D:\pic\heat.jpg',1)
    #cv2.imread() ：这个函数用于读入图片，应输入两个参数：图片路径，显示模式。
    #返回一个nparray（NumPy中的数组，与python自带的list有很多不同，此处暂且不提）。
    #显示模式有三种，分别是： 色彩模式——1， 灰度模式——0，带透明度参数模式—— -1. 输入模式对应的数字，或者直接使用常量：
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    #cv2.namedWindow() ：这个没什么好介绍的，就是初始化一个窗口。
    cv2.imshow('image',img)
    #cv2.imshow() : 这个函数用于在窗口中显示图片，有两个参数 ：窗口名称与图片变量。
    #此处的变量来自函数（1）的返回值，是一个nparray。
    cv2.waitKey(0)
    #cv2.waitKey(0) ：这个函数是一个绑定键盘动作的函数，它的参数是一个数字，表示在相应的毫秒之后监听键盘动作。
    #我觉得它就是加入了一个阻塞，满足条件之后解除阻塞，执行之后的语句。
    cv2.destroyAllWindows()
    #cv2.destroyAllWindows() ： 这个函数就是关闭窗口，
    #和（4）连起来就是按下任意键关闭显示图片的窗口。


    
    #接下来，我们用matplotlib显示图片
    img2 = cv2.imread('D:\pic\yosemeti.jpg')
    plt.imshow(img2,cmap='gray',interpolation='bicubic')
    #plt.imshow(): 这个函数用于将图片放入显示窗口中，但并不会弹出窗口。
    #有三个参数：图像的nparray，显示类型cmap以及插值算法。
    #前两个参数前面介绍过了。第三个参数是用于选择插值算法，
    #填补图像由于拉伸放大造成的不平滑的像素块，保持一定的图片质量。
    #此处选择的是双三次插值算法，是一种精度很高但速度偏慢的算法。
    plt.show()
    #cv2.imread()读入彩色图像时，返回的nparray是按照B,G,R的顺序排列的，
    #而matplotlib中的plt.imshow()显示彩色图像时，是按照RGB的顺序显示的，
    #因此就会造成红蓝色的错乱
    
    