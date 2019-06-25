#!/usr/bin/env python
# _*_ coding:utf-8 _*_


from copy import deepcopy
import csv,os,sys

class CSV_DataDeal:

    def __init__(self,dir_path:str,target:str):
        self.dir_path = dir_path
        self.target = target
        self.allfile = self.Read_All_File(dir_path)
        self.content = list()# 可以从这里获取修改前后一个表格的数据

    # 读取一个文件夹下面的所有的文件
    def Read_All_File(self,dir_path) -> list:
        if os.path.isdir(self.dir_path): # 判断存在文件夹
            allfile=os.listdir(dir_path)
            return allfile
        else:
            print("输入的路径不存在！")
            sys.exit(-1)

    # 读取一个文件夹下面的所有内容
    def ReadContent(self,filename):
        with open(filename, 'r') as fo:
            csv_object = csv.reader(fo)
            for row in csv_object:
                temp = list()
                for col in row:
                    temp.append(deepcopy(col))
                self.content.append(temp)

    # 把指定的值转换为0，返回修改后的csv.reader 对象
    def Change_To_Zero(self,target='1.7976930000000008e+308'):
        if self.target != target:
            self.target = target
        if self.content==[]:
            print("抱歉，您还没有数据可以处理，需要读取CSV文件")
            sys.exit('-1')
        else:
            for i,data in enumerate(self.content):
                for j,d in enumerate(data):
                    if d==self.target:
                        self.content[i][j]='0'

    def Write_File(self,filename:str):
        # 判断是否存在这个文件
        #newlise=''必须有否则会产生空行
        with open(filename, 'w',newline='') as f:
            csv_write = csv.writer(f, dialect='excel') # 设定写入模式
            for row in self.content:# 写入具体内容
                csv_write.writerow(deepcopy(row))
        return 1 # 写入成功

    # 处理所有的文件然后把内容存在原来的位置
    def Deal_And_Store(self,isStore=False):
        for f in self.allfile:
            filename= path+f
            print('正在处理文件：',filename)
            self.content.clear() #清除原来文件的内容
            self.ReadContent(filename)
            self.Change_To_Zero()
            if isStore:
                self.Write_File(filename)

# 看下面这个用法可以快速了解用法
if __name__ == '__main__':
    # path = "F:\\20190401\\cffex_IF1904.csv"
    import time
    t1 = time.time()
    path = "F:\\20190401\\"
    o = CSV_DataDeal(path,target='1.7976930000000008e+308')
    o.Deal_And_Store(True) #参数是是否存储，默认不存储
    t2 = time.time()
    print(t2-t1)

    # 也可自己组合：一次处理一个文件，要想处理多个需要多次读取，对应的处理每一次。
    #               如果一次读取数据过多可能会处理变慢 :）
    # 1、创建这个对象就已经获得了 本文件夹的所有的 ： 文件名allfile
    # 2、调用Change_To_Zero(target)方法可以把你指定的对象改为0 ，
    #       默认是把1.7976930000000008e+308改为0，修改后还是在content中
    # 3、可以选择存储 Write_File(filename) : filename包含 文件夹 和 文件名(没有检查是否有这个路径)
