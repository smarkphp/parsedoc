# -*- coding: utf-8 -*-
import os
import json
# import sys
# reload(sys)   
# sys.setdefaultencoding('utf8') 

''' --解析txt文件--'''
class txt:

    @staticmethod
    def readTxt1(file,keyv):
        print(">>> readTxt1")
        f = open(file)
        line = f.readline()
        while line:
            if keyv in line:
                print(line)
            line=f.readline()
        f.close()


    @staticmethod
    def readTxt2(file,keyv):
        print(">>> radTxt2")
        # f = open(file)
        for line2 in open(file):
            if keyv in line2:
                print(line2)


    @staticmethod
    def readTxt3(file,keyv):
        print(">>> readTxt3")
        i = 1
        f2 = open(file,"r")
        lines = f2.readlines()
        for line3 in lines:
            if keyv in line3:

                print(i,line3)
                i=i+1
    

''' --解析java源代码--同txt文档'''
class tjava:

    @staticmethod
    def readJa():
        print(">>--ja")

class tIni:

    @staticmethod
    def readIni():
        print(">>---ini")

class mulPro:
    
    dirs=[]
    files=[]

    """具体目录下的文件查找汇总"""
    @staticmethod
    def traversal_files(path):
        for item in os.scandir(path):
            if item.is_dir():
                # print(item,type(item))
                mulPro.dirs.append(item.path)
            elif item.is_file():
                if item.path.split("/")[-1][0:1] ==  ".":   # 去除隐藏文件
                    continue
                else:
                    mulPro.files.append(item.path)
        print("dirs: ",mulPro.dirs)
        print("files: ", mulPro.files)



    """递归遍历目下下所有文件查找指定文件:包含了隐藏文件"""
  
    flv=[]
    @staticmethod
    def search(root, target):
        items = os.listdir(root)
        
        for item in items:
            path=os.path.join(root,item)
            if os.path.isdir(path):            
                if path.split("/")[-1][0:1] == ".":    # 去除隐藏的文件夹，递归调用
                    continue
                else:
                    mulPro.search(path,target)
                    
                # print('[---]', path)
            elif path.split('/')[-1] == target:       # 目标文件、现在只是打印 TODO: 后面加入目标文件的遍历
                print('[dest File====]:', path) 
            else:
                if path.split("/")[-1][0:1] == ".":    # 去除隐藏的文件
                    continue
                else:
                    # print('[!]', path)               # 正常文件
                    global flv
                    mulPro.flv.append(path)

        # print(">>all files: ", mulPro.flv)
        return  mulPro.flv
      

    """指定工程下文件中具体内容数据查找<不包含: 隐藏文件夹 和 指定文件夹>"""
    @staticmethod
    def destCodeScan(filep, destFile,destV):
        print('指定代码工程 {project} 目下文件扫描'.format(project=filep))
        # 去除隐藏文件、形成文件列表
        for root, dirs, files in os.walk(filep):
            files = [f for f in files if not f[0] == '.']
            dirs[:] = [d for d in dirs if not d[0] == '.']

            # ----文件结果的统计
            fileLst = []

            dictO = {}                     # 遍历结果大字典
            dictO[destV] = {}

            for file_name in files:
                fileLst.append(os.path.join(root, file_name))
                # print(os.path.join(root, file_name))

            # 具体文件解析
            i = 0                         # 总行记录字段
            for fle in fileLst:               # 文件
                fb = open(fle,  "r")
                lines = fb.readlines()
                j = 0                        #  匹配行记录字段
                dictFle = {}            #每一个文件的具体内容
                dictle = {}             # 每一个文件每一行的具体内容

                fp = fle.split("\\")
                fpName = fp[-1]

                for lie in lines:           # 行
                    j = j + 1
                    i = i + 1
                    # print(fle, ':', lie)
                    #---对文件取具体名称、正则匹配

                    destVc = re.compile(destV, re.I)
                    match = destVc.search(lie)

                    if match:
                        # print("文件: ",fpName, j ,"行 ,", "内容: ", lie, '匹配:', match.group())
                        lineV=str(j)+"行内容"
                        dictVline = {lineV: lie}
                        # print(dictVline)
                        dictle.update(dictVline)  # 每一行的具体内容累加更新
                    else:
                        continue
                dictFle[fpName] = dictle       # 每-个文件的内容赋值
                # print("dle: ",dictFle)
                dictO[destV].update(dictFle)  # 总体工程文件更新
            print("遍历文件总行数: ",i)

            print(dictO)
            # 写入到具体文件目录下: 文件名
            print("fpname",destFile)
            with open(destFile+".json", "w") as code:
                code.write(json.dumps(dictO))
            return dictO


if __name__ == "__main__":
    # txt.sum(3,4)
    # txt.readTxt1("../file/txt/abc.txt","兴趣")
    # txt.readTxt2("../file/txt/abc.txt","兴趣")
    # txt.readTxt3("../file/txt/abc.txt","兴趣")
    # txt.readTxt3("../file/txt/debuglog.txt","xxxxdddd a=1 b=2 test=test3 sss")

    # txt.readTxt3("../file/java/HelloWorld.java","sum")

    #  txt.readTxt2("../file/ini/pytest.ini","py.xml")
    filePro="/Users/mark1117/sourceDocCode/gitCompany/gitCeba/pdoc/pdocp"
    # mulPro.destCodeScan(filePro,"/Users/mark1117/sourceDocCode/gitCompany/gitCeba/pdoc/pdocp/res","addopts")

  
    flvv = mulPro.search(filePro,'der.docx')
    print(">>flvv: ",flvv,"\n length is: ", len(flvv))

    # mulPro.traversal_files(filePro)


