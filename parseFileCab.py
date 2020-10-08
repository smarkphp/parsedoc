# -*- coding: utf-8 -*-
'''
Desccription: 
version: 
company: zy
Author: Mark
Date: 2020-10-03 16:22:23
ListenEditors: Mark
LastEditTime: 2020-10-07 11:33:22
zip:
    1、https://www.cnblogs.com/ctztake/p/9141259.html
    2、https://blog.csdn.net/qq_24499417/article/details/82155926
    3、https://www.kancloud.cn/thinkphp/python-cookbook/37060
jar:
    4、具体划分: https://blog.csdn.net/u013692888/article/details/75011528 
    
    5、标准方式: https://learnku.com/docs/pymotw/zipfile-zip-archive-access/3414
war:

TODO:
    1、压缩包中最后扫描的是文件(做记忆处理)，如果有目录(如果解压最后要清除rm-rf掉)、则要剔除掉、最后要做文件扫描统一处理
    2、会不会有递归引入外部jar包的情况,有！外部引入的不考虑.
Other: 其它压缩包的情况: gz、zip、rar
    3、https://blog.csdn.net/lyd0813/article/details/78148709

'''
import zipfile
import os
# import tensorflow as tf
import parseFilePdf
import io

class  parseCp:

    ''' linux command: zip -q -r test.zip * (* 是具体文件目录) 中文乱码，如果用python zip解压就没问题'''
    @staticmethod
    def zipWrite():
        print("zip写入")
        #----SectionI
        # for root, dirs, files in os.walk('../file/zip'):
            # print(">>====",os.getcwd())
            # print('>>root',root)
            # print('>>dir',dirs)
            # print('>>files:',files,'>>type:',type(files))
            # for fn in files:
                # print(fn.strip(), type(fn))
                
        #----SectionII
        os.system("rm -rf ../file/zip/test2.zip")
        zip = zipfile.ZipFile('../file/zip/test2.zip','w',zipfile.ZIP_DEFLATED) 
        # #往里面写入内容
        for root, dirs, files in os.walk('../file/zip'):
            for fn in files:
                if 'zip' not in fn:
                    print('../file/zip/'+fn)
                    zip.write('../file/zip/'+fn,compress_type=zipfile.ZIP_DEFLATED)
        zip.close()


    @staticmethod
    def zipRead():
        print("zip读取")

        zf = zipfile.ZipFile('../file/zip/test2.zip')
        print(zf.filename,'文件内容列表长度: ', len(zf.namelist()))
        for filename in zf.namelist():
            print("filename: ",filename,',suffix: ',filename.split(".")[-1])
            if filename.split(".")[-1] == "docx":
                fn = filename
            # print(filename.encode('cp437'))
            # print(filename.encode('cp437').decode('gbk'))  #----TODO这块儿文件名解压有问题
        print("filename:",fn)
        """判断不同文件后缀不同方式去解析--"""

        zz_info = zf.getinfo(fn)
        print(zz_info)
        # 读取第一个文件的内容:
        ft = zf.read(fn)
        print('has',len(ft),'bytes','type is: ',type(ft))

        # ---method1():

        with zf.open(fn) as zfo:
            print(zfo.read().decode)
        # with io.TextIOWrapper(zf.open(fn),encoding="utf-8") as f:

        # ---method1(): 第一种方法: 非解压直接读取、但目前只是适合xml文件形式
        # ---step1: 读取

        # ft = zf.read(fn)
        # print(ft.decode('utf-8'), '\n',type(ft.decode('utf-8')),'\n',)  #-----如果是pdf,docx则打出的内容是bytes乱码

        # ---step2: 判断
        # if "Zope" in ft.decode('utf-8'):
        #     print("ok -zope in it")

        # ----method2(): 第二种方法: 解压到具体的文件再具体调用其解压的方法
        # zf.extractall()
        parseFilePdf.pdf.read("../file/pdf/投标文件.pdf", "孙国权")

        zf.close()
        
    @staticmethod
    def readJar():
        print(">>>parseJar<<")
        # zf = zipfile.ZipFile('../file/jar/HelloWorld.jar')

        zf = zipfile.ZipFile('../file/war/jenkins.war') # 也支持war包

        print(zf.filename, '文件内容列表长度: ', len(zf.namelist()))
        for filename in zf.namelist():
            # print(filename,'sfix: ',)
            if filename[-1:] == "/":
                print("目录: ", filename)
            else:
                print("文件: ",filename)

            # if filename.split(".")[-1] == "class":
            #     fn = filename
        # print(fn)

        # with zf.open(fn) as zfo:
        #     print(zfo.read().decode())  #.class 文件也不可以读取, 也还是字节码

        # os.system('mkdir jar')
        # zf.extractall('./jar')
        # os.system('rm -rf jar')

    '''--同war包---'''
    @staticmethod
    def readWar():
        print("parseWar")



if __name__ == "__main__":
    # parseFilePdf.pdf.read("../file/pdf/投标文件.pdf", "孙国权")
    # parseCp.zipWrite()
    # parseCp.zipRead()
    parseCp.readJar()