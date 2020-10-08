'''
Desccription: 
version: 
company: zy
Author: Mark
Date: 2020-10-08 10:31:33
ListenEditors: Mark
LastEditTime: 2020-10-08 17:45:37
#--
'''
# -*- coding:UTF-8 -*-
import os
import re 
import json

class cpv:

    @staticmethod
    def pv(key,**args):
        print(key,type(key))
        print(args,type(args))


    @staticmethod
    def pth():
        print("dm:", os.path.dirname(__file__))
        print("dm2:",os.path.dirname(os.path.dirname(__file__)))

    """--json--"""
    @staticmethod
    def json_dmp():
        data={
                "msgBody":{
                        "data":
                            {
                                "imgType": "",
                                "imgURL": "image url",
                                "imgLike": 0.5
                            }
                    },
                "msgHead":{
                        "Token": "",
                        "Code": "",
                        "rmsg": "你好",
                    }
            }
            
        data_1=json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'),ensure_ascii=False)
        print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ':')))


    """1、 https://blog.csdn.net/mieleizhi0522/article/details/82142856"""
    """2、 https://blog.csdn.net/alvine008/article/details/43410079?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param"""
    """3、https://www.cnblogs.com/ellisonzhang/p/10273843.html"""
    """4、https://github.com/seeways/PythonDemo/blob/master/static/yield_demo.py"""
    @staticmethod
    def yield_foo():
        print("starting...")
        while True:
            res = yield 4
            print("res:",res)

    """yeild from: https://www.cnblogs.com/wongbingming/p/9085268.html"""      
    @staticmethod
    def yeild_gen():
        # 字符串
        astr='ABC'
        # 列表
        alist=[1,2,3]
        # 字典
        adict={"name":"wangbm","age":18}
        # 生成器
        agen=(i for i in range(4,8))
        
        # ----Section I
        # def gen(*args, **kw):
        #     for item in args:
        #         # print("item:",item)
        #         for i in item:
        #             yield i 
        #             # pass
        
        # new_list=gen(astr, alist, adict, agen)
        # print(list(new_list))

        # ----Seciton II
        def gen(*args, **kw):
                for item in args:
                    yield from item

        new_list=gen(astr, alist, adict, agen)
        print(list(new_list))
    """---正则---"""
    @staticmethod
    def re_1():
        regex = r"([a-zA-Z]+) (\d+)"
        match = re.search(regex, "I was born on June 24") 
        if match != None:  
             print("Match at index % s, % s" % (match.start(), match.end())) 
             
             print(match.group(2))
             
             print("Full match: % s" % (match.group(0))) 
             print("Month: % s" % (match.group(1))) 
             print("Day: % s" % (match.group(2))) 


    @staticmethod
    def re_2():
        string = """Hello my Number iis 123456789 and  my friend's number is 987654321"""
        regex = 'i.s \d+'          #-- + . * 的不同操作
        match = re.findall(regex, string)
        print(match)


  
    
if __name__ == "__main__":
    # cpv.pv(1,[1,2])
    # cpv.pth()
    # cpv.re_2()
    
    # g=cpv.yield_foo()
    # print(next(g))
    # print("*"*20)
    # print(next(g))

    # cpv.yeild_gen()
   