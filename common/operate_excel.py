import xlrd
from xlutils.copy import copy


class OperateExcel(object):
    def __init__(self, file_name=None, sheet_id=None):
        """
        :param file_name: excel文件的具体路径名称
        :param sheet_id:  要操作的第几 sheet 页
        """
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = '../operate_excel.xls'

        if sheet_id:
            self.sheet_id = sheet_id
        else:
            self.sheet_id = 0

        self.sheet_table = self.get_sheet()

    # 获取 sheet 页操作对象
    def get_sheet(self):
        data = xlrd.open_workbook(self.file_name)
        sheet_table = data.sheets()[self.sheet_id]
        return sheet_table

    # 获取该 sheet 页的行数和列数，拿到的是一个元组
    def get_sheet_nrows_ncols(self):
        return self.sheet_table.nrows, self.sheet_table.ncols

    # 获取该 sheet 页的行数
    def get_sheet_nrows(self):
        return self.sheet_table.nrows

    # 获取该 sheet 页的列数
    def get_sheet_ncols(self):
        return self.sheet_table.ncols

    # 获取具体单元格的数据
    def get_sheet_cell(self, row, col):
        """
        :param row: 单元格的行值
        :param col: 单元格的列值
        :return: cell_data
        """
        cell_data = self.sheet_table.cell_value(row, col)
        return cell_data

    # 写入数据到 excel 中
    def write_to_excel(self, row, col, value, sheet_id):
        # 同样的先打开 excel 操作句柄
        data = xlrd.open_workbook(self.file_name)
        copy_data = copy(data)
        # 选择写入的 sheet 页
        copy_data_sheet = copy_data.get_sheet(sheet_id)
        # 写入数据
        copy_data_sheet.write(row, col, value)
        # 保存数据
        copy_data.save(self.file_name)


if __name__ == "__main__":
    oe = OperateExcel()
    print("获取 excel 表的行数和列表，返回元组形式：", oe.get_sheet_nrows_ncols())
    print("获取 excel 表的行数：", oe.get_sheet_nrows())
    print("获取 excel 表的列数：", oe.get_sheet_ncols())
    print("获取单元格(1, 1)的值：", oe.get_sheet_cell(4, 0))
    print("获取单元格(1, 2)的值：", oe.get_sheet_cell(6, 1))
    # print("获取单元格(2, 2)的值：", oe.get_sheet_cell(2, 2))
    oe.write_to_excel(6, 1, '写入的数据', 1)