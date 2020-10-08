'''
Desccription: 
version: 
company: zy
Author: Mark
Date: 2020-10-08 17:46:01
ListenEditors: Mark
LastEditTime: 2020-10-08 18:02:22
'''


class secu:

    @staticmethod
    def apply(func,*args,**kargs):
        print("...func apply check...")

    @staticmethod
    def noargs_fun():
        print("No args functions")
    
    @staticmethod
    def tup_fun(arg1, arg2):
        print(arg1,arg2)

    @staticmethod
    def dic_fun(arg1=1,arg2=2):
        print(arg1, arg2)

        
if __name__ == "__main__":
    # secu.apply(secu.noargs_fun)
    
    # secu.apply(secu.tup_fun("参数1","参数2"))

    kw={"arg1":"参数11","arg2":"参数21"}
    # print(kw)
    secu.apply(secu.dic_fun,(),kw)