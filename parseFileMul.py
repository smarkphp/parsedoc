
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

if __name__ == "__main__":
    # txt.sum(3,4)
    # txt.readTxt1("../file/txt/abc.txt","兴趣")
    # txt.readTxt2("../file/txt/abc.txt","兴趣")
    # txt.readTxt3("../file/txt/abc.txt","兴趣")
    txt.readTxt3("../file/txt/debuglog.txt","xxxxdddd a=1 b=2 test=test3 sss")

    # txt.readTxt3("../file/java/HelloWorld.java","sum")

    #  txt.readTxt2("../file/ini/pytest.ini","py.xml")

