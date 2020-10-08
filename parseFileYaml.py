'''
Desccription: 
version: 
company: zy
Author: Mark
Date: 2020-10-03 09:42:46
ListenEditors: Mark
LastEditTime: 2020-10-03 10:46:59
思想: yaml转换正json
link: https://www.cnblogs.com/xiao-erge112700/p/11943591.html

1、for key in a:
2、for key in a.keys():
3、for value in a.values():
4、for kv in a.items():
5、for key,value in a.items():
6、for (key,value) in a.items():
'''
import os
import yaml

class parseyml:

    @staticmethod
    def writes(yampath):
        data = {'school':'erxiao',
                'students':['lili','jj']}
        file = open(yampath,'w',encoding='utf-8')
        yaml.dump(data,file)
        file.close()

        

    @staticmethod
    def readm():
        print(">>读取多个文件")
        yaml.warnings({'YANMLLoadWarning':False})
        f = open('../file/yaml/ymlm.yaml','r',encoding='utf-8') # 打开yaml文件
        cfg = f.read()
        d = yaml.load_all(cfg)  # 将数据转换成python字典形式输出，存在多个文件时，用load_all, 单个的时候load就可以
        for data in d:
            print(data)
        f.close()


    ''' --遍历到key-- 其值可能是dict、也可能是list'''
    @staticmethod
    def reads(file,keyp):
        print(">>读取单个文件")
        yaml.warnings({'YANMLLoadWarning':False})
        f = open(file,'r',encoding='utf-8') # 打开yaml文件
        cfg = f.read()
        d = yaml.load(cfg)
        # print(d)
        # print(type(d))

        for key in d:
            # print(key)
            if key in keyp:
                print(key+':'+d[keyp])
        f.close()

if __name__ == "__main__":

    # currentpath=os.path.abspath('.')     #获取当前路径
    # print(currentpath)
    # yamlpath=os.path.join(currentpath,'generate.yaml')    #创建yaml文件
    # parseyml.writes(yamlpath)
    
    # parseyml.readm()
    parseyml.reads('../file/yaml/ym1.yaml','user')
