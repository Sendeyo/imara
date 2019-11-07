import datetime
import data
import os
import xlrd
import xlwt

workingDir = os.getcwd()


def Read(path, filename, validators):
    os.chdir(workingDir)
    location = os.path.join(os.getcwd(), path)
    os.chdir(location)
    print(os.listdir('.'))
    if filename in os.listdir('.'):
        book = xlrd.open_workbook(os.path.join(location, filename))
        sheet = book.sheet_by_index(0)
        print("rows: {} , columns: {}".format(sheet.nrows, sheet.ncols))
        if sheet.nrows < 1:
            print("No content")
            return "This file has no content"
        columns = []
        for x in range(0, sheet.ncols):
            columns.append(sheet.cell_value(0,x))
        if str(columns) == validators:
            data = []
            for y in range(1, sheet.nrows):
                row = []
                for x in range(0, sheet.ncols):
                    try:
                        if x == 4:
                            value = str(int(sheet.cell_value(y,x)))
                            if value[0] == "7":
                                val = "{}{}".format("+254", value)
                        else:
                            val = int(sheet.cell_value(y,x))
                            
                    except:
                        val = sheet.cell_value(y,x)
                    row.append(val)
                data.append(row)
            os.remove(filename)
            os.chdir(workingDir)
            return data
    else:
        print ("No such file")
    

def Create_collection_sheet():
    location = "static/downloads"
    file = "collection.xlsm"
    date = datetime.datetime.now()
    structure = ["Id","Member_no"]
    os.chdir(workingDir)
    location = os.path.join(workingDir, location)
    os.chdir(location)
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet("Sheet1")
    worksheet.write(0,0, "Month")
    worksheet.write(0,1, "{}-{}".format(date.month, date.year))
    y = 1
    x = 0
    for item in structure:
        worksheet.write(y,x, item)
        x+=1
    for day in range(1, 32):
        worksheet.write(y,x, day)
        x+=1
    workbook.save(file)
    return "success"


print(Create_collection_sheet())
    
    


# cwd = os.getcwd()
# filename = "members.xlsm"
# location = "static/uploads"
# document = "{}/{}/{}".format(cwd, location, filename)
# print(document)
# files = os.listdir(".")
# print(files)
# # if filename in files:
# #     print("This will work")
# #     # open workbook
# #     book = xlrd.open_workbook(document)
# #     # sheet = book.sheet_by_index(0)
# #     sheet = book.sheet_by_name("MAIN")
# #     print("rows: {} , columns: {}".format(sheet.ncols, sheet.nrows))




def Add_to_db(Member_no, National_id, Name, Station, Phone_no):
    query = 'insert into Member_Basic_info (Member_no, National_id, Name, Station, Phone_no) values ("{}","{}","{}","{}","{}")'.format(Member_no, National_id, Name, Station, Phone_no)
    print(query)
    data.data_write(query)
    



   
