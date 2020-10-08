# -*- coding:UTF-8 -*-
"""
@Project: pdoc   #项目名称
@Description: TODO          #描述
@Time:2020/10/4 4:51 下午       #日期
@Author:mark1117                #创建人

"""

class cpv:

    @staticmethod
    def pv(key,**args):
        print(key,type(key))
        print(args,type(args))


if __name__ == "__main__":
    cpv.pv(1,[1,2])