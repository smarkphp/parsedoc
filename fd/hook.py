# coding=utf-8

import func
from hook2 import secu

def _hook_show(*args,**kwargs):
    # to do hook
    print("hook show func")
    realfun, = args 
    return secu.apply(realfun)

def hook():
    _show = func.show()
    # print("_show: ",_show)
    func.show = lambda :secu.apply(_hook_show,(_show,)) 


if __name__ == "__main__":
    hook()
    func.show()