'''
Desccription: 
version: 
company: zy
Author: Mark
Date: 2020-10-03 10:47:46
ListenEditors: Mark
LastEditTime: 2020-10-03 17:11:29
Goal： xml解析
link: 
1、https://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p03_parse_simple_xml_data.html
2、更新:> https://www.cnblogs.com/xiaobingqianrui/p/8405813.html


'''
# 通过minidom解析xml文件
import xml.dom.minidom as xmldom
import os
#
import xml.etree.ElementTree as ET 
import sys

class parseXml:


    @staticmethod
    def reads1(file):
        print(">>parse 通过minidom解析xml文件<<")
        xmlfilePath = os.path.abspath(file)
        print(xmlfilePath)
        # 得到文档对象
        domobj = xmldom.parse(xmlfilePath)
        # print("xmldom.parse:", type(domobj))

        # 得到元素对象
        elementobj = domobj.documentElement
        # print ("domobj.documentElement:", type(elementobj))

        # step1.1: 获得子标签: 及其对应的属性值
        subElementObj = elementobj.getElementsByTagName("login")
        print ("getElementsByTagName:", type(subElementObj))
        print (len(subElementObj))

        # step1.2: 获得标签: 属性值
        print (subElementObj[0].getAttribute("username"))
        print (subElementObj[0].getAttribute("passwd"))
        
        #区分相同标签名的标签>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        subElementObj1 = elementobj.getElementsByTagName("caption")
        for i in range(len(subElementObj1)):
            # print ("subElementObj1[i]:", type(subElementObj1[i]))
            print ("sfd:"+subElementObj1[i].firstChild.data)  #显示标签对之间的数据


    @staticmethod
    def readsAndMod2(file):
        print("ElementTree:{xml.etree.ElementTree} || xml.etree.cElementTree")
        """
        a. 遍历根节点的下一层　　　
    　　 b. 下标访问各个标签、属性、文本
    　　 c. 查找root下的指定标签
    　　 d. 遍历XML文件
    　　 e. 修改XML文件
        """

        def traverseXml(element):
            # print(len(element))
            if len(element) > 0:
                for child in element:
                    print(child.tag,'---',child.attrib,'--',child.text)
                    traverseXml(child)
        
        xmlFilePath = os.path.abspath(file)
        print(xmlFilePath)

        try:
            tree = ET.parse(xmlFilePath)            #----step1: ET读取
            # print("tree type: ",type(tree))
            # 获得根结点
            root = tree.getroot()                   #----step2: 获取根结点
        except expression as identifier:
            print("parse "+file+" fail!")
            sys.exit()
        # print("root type: ",type(root))
        print("root层",root.tag,"---", root.attrib)

        # 遍历root的下一层
        for child in root:                          #----step3:root遍历
            print ("遍历root的下一层", child.tag, "----", child.attrib)
        # 使用下标访问
        print(root[0].text)
        print(root[1][0].text)
        print(root[1][1][0].text)

            
        # >>>> --SectionII 遍历xml文件
        print(20 * "*")  
        traverseXml(root)                           #----step3.1: root遍历
        print(20 * "*")

        # >>>> --SecttionIII 根据签名找root下的所有标签
        captionList = root.findall("item")          #----step其它: 寻找指定元素
        # print(len(captionList))  
        for caption in captionList:
            print(caption.tag,"----",caption.attrib,"----",caption.text)

        # >>>> --SectionIV
        login = root.find("login")
        passwowdValue = root.find("passwd")
        print("not modify passwd: ", passwowdValue)    
        login.set("passwd","999999999")
        # login.text("passwd","8888")
        print("modify passwd: ", login.get("passwd"))
        

    
    @staticmethod
    def read(file, destv):
        
        def traverseXml(element):
            # print(len(element))
            if len(element) > 0:
                for child in element:
                    # print(child.tag,'---',child.attrib,'--',child.text)
                    if destv in child.text:
                        print(">>",child.text)
                    # if destv in child.tag:              #TODO: 这块儿逻辑还要处理：标签、属性、文本 可能是三处查找
                    #     print('>>',child.tag,'---',child.attrib,'--',child.text)
                    #     print(child.tag,'--',child.attrib,'--',child.attrib['protocol'])
                    traverseXml(child)

        xmlFilePath = os.path.abspath(file)
        print(xmlFilePath)

        try:
            tree = ET.parse(xmlFilePath)            #----step1: ET读取
            # print("tree type: ",type(tree))
            # 获得根结点
            root = tree.getroot()                   #----step2: 获取根结点
        except expression as identifier:
            print("parse "+file+" fail!")
            sys.exit()
        # print("root type: ",type(root))
        print("root层",root.tag,"---", root.attrib)

        print(20 * "*")  
        traverseXml(root)                           #----step3.1: root遍历
        print(20 * "*")



        
    @staticmethod
    def writes():
        print("<<write")


if __name__ == "__main__":
    # parseXml.reads('../file/xml/test.xml')
    # parseXml.readsAndMod2('../file/xml/test.xml')

    parseXml.read('../file/xml/test.xml','dasdas')
    # parseXml.read('../file/xml/server.xml', 'Connector')