import xlrd
import os

file_path = "D:\Mywork\合规工作流程20180711.xls"
rlf_path = "D:\\MyProjects\\xinan_bank_sys_test\\data_test\\register_login_forgetpw.xls"



# 从excel读取登录的信息
def read_login_data(row_num):
    # 打开文件
    workbook = xlrd.open_workbook(file_path)

    sheet1 = workbook.sheet_by_name('登录账号')

    username = int(sheet1.cell_value(row_num - 1, 1))
    password = sheet1.cell_value(row_num - 1, 4)
    return username, password


# 从excel读取注册的相关信息
def read_register_data(row_num):
    workbook = xlrd.open_workbook(file_path)
    sheet1 = workbook.sheet_by_name('登录账号')
    mobile = int(sheet1.cell_value(row_num - 1, 1))
    password = sheet1.cell_value(row_num - 1, 2)
    return mobile, password


def read_sheet_data(row_num):
    workbook = xlrd.open_workbook(file_path)
    sheet1 = workbook.sheet_by_name('data')
    result = sheet1.cell_value(row_num-1,1)
    return result

def read_sheet_expect_data(row_num):
    workbook = xlrd.open_workbook(file_path)
    sheet1 = workbook.sheet_by_name('data')
    result = sheet1.cell_value(row_num-1,2)
    return result


# Register_Login_ForgetPW
def read_excel_for_rlf(row_num):
    workbook = xlrd.open_workbook(rlf_path)
    sheet1 = workbook.sheet_by_name('sheet1')
    data_register = sheet1.cell_value(row_num - 1, 1)
    target_result = sheet1.cell_value(row_num-1,3)
    return data_register,target_result




# r = read_excel_for_rlf(2)
# print(r)
