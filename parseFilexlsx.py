'''
Desccription: 
version: 
company: zy
Author: Mark
Date: 2020-11-25 22:00:10
ListenEditors: Mark
LastEditTime: 2020-11-25 22:02:27
'''


class scanXlsx:

    """
    写入excel
    """
    @staticmethod
    def writeResAsXlsM(saveFile, content):
        print("将数据保存至xlsx文件")

        f = openpyxl.Workbook()
        table = f.active
        table.title = '其他文件统计结果'

        table.cell(row=1, column=1, value="文件")
        table.cell(row=1, column=2, value="行位置")
        table.cell(row=1, column=3, value="内容")

        j=1
        for contente in content:
            print(",,",contente,'type',type(contente))
            file = contente['file']
            # print(contente['content'])
            for k, v in contente['content'].items():
                print(k,'-',v)
                j=j+1
                table.cell(row=j, column=1, value=file)
                table.cell(row=j, column=2, value=k)
                table.cell(row=j, column=3, value=v)

        # 保存文件
        ct = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        f.save(saveFile +ct+ ".xlsx")

    """
    写入excel
    """
    @staticmdthod
    def writeResXlsMulSheet(destfile, destV, dictO):
            print("将数据写入到一个文件，多个sheet")
            wb = openpyxl.Workbook()

            for file in dictO[destV]:
                fileContent = dictO[destV][file]
                if len(fileContent) != 0:
                    # print(fileContent)
                    sheet = wb.create_sheet(file)
                    row_col = ["行数", "内容"]
                    sheet.append(row_col)
                    for k, v in fileContent.items():
                        print(k,v)
                        row_data = [k , v]
                        sheet.append(row_data)
            ct = time.strftime("%Y%m%d_%H%M%S", time.localtime())
            wb.save(destfile+ct +".xlsx")

if __name__ == "__main__":
    print(">>>>")
