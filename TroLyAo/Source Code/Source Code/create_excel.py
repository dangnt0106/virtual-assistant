# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import openpyxl


# Tạo tệp tin excel.
def create_excel(input_detail, output_excel_path):

    # Xác định số hàng và cột lớn nhất trong file excel cần tạo.
    row = len(input_detail)
    column = len(input_detail[0])

    # Tạo một workbook mới và active nó.
    wb = openpyxl.Workbook()
    ws = wb.active

    # Dùng vòng lặp for để ghi nội dung từ input_detail vào file Excel.
    for i in range(0, row):
        for j in range(0, column):
            v = input_detail[i][j]
            ws.cell(column=j + 1, row=i + 1, value=v)

    # Lưu lại file Excel.
    wb.save(output_excel_path)


# create_excel()