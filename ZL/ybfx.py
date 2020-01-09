# import requests
# login_url = 'http://58.242.186.52:7005/nybdata/login?user_name=15200808387&pwd=1'
# header = {
#     "Content-Type": 'application/json',
# }
# login = requests.post(url=login_url, headers=header)
#
# token = login.json()["datas"]["token"]
# cookies = login.cookies
# print(type(token))
# print(token)
# print(login.headers)
# print(login.url)
# print(login.cookies)
# header_new = {
#     "token": token,
#     "Content-Type": 'application/json',
# }
#
# ybfx_url = 'http://58.242.186.52:7005/nybdata/getSoilListPage?corp=&soil_plot_name=&col_point_code=&batch=&act_date_beg=&act_date_end=&pageNum=1&pageSize=10'
# # ybfx = requests.get(ybfx_url,headers={"token":token,"Content-Type": 'application/json'})
# ybfx = requests.get(ybfx_url,headers=header_new)
# print(ybfx.json())

# 不同.py文件调用函数
# import sys
#
# sys.path.append(r'/Users/chenjiawei/PycharmProjects/untitled')
# import zhonglian
#
# print(zhonglian.login_token())


import xlrd


# def read_file():
#     try:
#         new_data = xlrd.open_workbook(r'/Users/chenjiawei/PycharmProjects/untitled/ZL/element.xlsx')
#         return new_data
#     except Exception as e:
#         print(str(e))
#     workbook = xlrd.open_workbook(r'/Users/chenjiawei/PycharmProjects/untitled/ZL/element.xlsx')
#     sheet_names=workbook.sheet_names()
#     print(sheet_names)
#
#     sheet1=workbook.sheet_by_name('A')
#     nrows=sheet1.nrows
#     ncols=sheet1.ncols
#     print(nrows,ncols)
#     cell_A=sheet1.cell(1,1).value
#     print(cell_A)
#
# if __name__ == '__mian__':
#     read_file()


# workbook = xlrd.open_workbook(r'/Users/chenjiawei/PycharmProjects/untitled/ZL/element.xlsx')
# sheet_names= workbook.sheet_names()
# print(sheet_names)
# for sheet_name in sheet_names:
#     sheet = workbook.sheet_by_name(sheet_name)
#     rows = sheet.nrows # 获取行数
#     cols = sheet.ncols # 获取列数，尽管没用到
#     all_content = []
#     for i in range(rows) :
#         cell = sheet.cell_value(i,0) # 取第二列数据
#         try:
#             cell = int(cell) # 转换为整数
#             all_content.append(cell)
#         except ValueError as e:
#             pass
#     # cols = sheet.col_values(2) # 获取第二列内容 但是整数会处理成float
#     print(all_content)


def readexcel():
    workbook = xlrd.open_workbook(r'/Users/chenjiawei/PycharmProjects/untitled/ZL/element.xlsx')
    sheet_names = workbook.sheet_names()
    print(workbook.sheet_names())
    sheet2 = workbook.sheet_by_name('A')
    nrows = sheet2.nrows
    ncols = sheet2.ncols
    print(nrows, ncols)

    cell_A = sheet2.cell(1, 1).value
    print(cell_A)


if __name__ == '__mian__':
    readexcel()
