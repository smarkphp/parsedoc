'''
Desccription: 
version: 
company: zy
Author: Mark
Date: 2020-10-02 11:51:39
ListenEditors: Mark
LastEditTime: 2020-10-03 09:43:16
link: https://www.cnblogs.com/gl1573/p/10064438.html
'''
import pdfplumber

class pdf:

    @staticmethod
    def write():
        print("write--")

    @staticmethod
    def read(path, keyword):
        # path = "../file/pdf/投标文件.pdf"
        pdf = pdfplumber.open(path)
        print("read---")
        
        i1 = 1
        j1 = 1
        for page in pdf.pages:
            # ======获取当前页面的全部信息:{文字}
            ptext = page.extract_text()    
            # print("page type: ",type(ptext)) 
            if keyword in ptext:
                print(ptext)
                print(type(ptext))
                print("i1 is:",i1)
                i1=i1+1
                
                print('--content page---')

            
            # =======获取当前页面全部信息: {表格}
            for table in page.extract_tables():
                
                for row in table:
                    # print(row)
                    if keyword in row:
                        print("j1 is:",j1)
                        print("row value: ",row,"\n",type(row))
                        j1=j1+1
                        print('---content table---')
              
        print("含有:", keyword, ",文字数: ",i1,"表格数:",j1)
        pdf.close()


if __name__ == "__main__":
    pdf.read("../file/pdf/投标文件.pdf","孙国权")