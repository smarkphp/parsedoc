'''
Desccription: 
version: 
company: zy
Author: Mark
Date: 2020-10-08 10:31:33
ListenEditors: Mark
LastEditTime: 2020-10-08 11:29:33
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
    cpv.re_2()