# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import os
from text_to_speech import speak
from get_text import get_text
from docx import Document
from create_excel import create_excel


# Tạo các loại file cho máy tính. Ở đây set cứng đường dẫn luôn.
def create_file():
    try:
        speak("Bạn muốn tạo loại file gì?")
        time.sleep(2.5)
        file_type = get_text()
        if "txt" in file_type or "note pad" in file_type or "ghi chú" in file_type:
            speak("Bạn muốn đặt tên file là gì?")
            time.sleep(3)
            name = get_text()
            file = open("D:\\Test\\Test File\\{file}.txt".format(
                file=name), "w", encoding="utf-8")
            speak("Bạn muốn ghi vào file nội dung gì?")
            time.sleep(3)
            content = get_text()
            file.write(content)
            file.close()
            speak("Đã tạo file. Dưới đây là đường dẫn tới file bạn vừa tạo.")
            time.sleep(5)
            print("Bot: D:\\Test\\Test File\\{file}.txt".format(file=name))
            os.startfile("D:\\Test\\Test File\\{file}.txt".format(file=name))
        elif "word" in file_type or "văn bản" in file_type:
            speak("Bạn muốn đặt tên file là gì?")
            time.sleep(3)
            name = get_text()
            document = Document()
            speak("Bạn muốn ghi vào file nội dung gì?")
            time.sleep(3)
            content = get_text()
            document.add_paragraph(content)
            document.save("D:\\Test\\Test File\\{file}.docx".format(file=name))
            speak("Đã tạo file. Dưới đây là đường dẫn tới file bạn vừa tạo.")
            time.sleep(5)
            print("Bot: D:\\Test\\Test File\\{file}.docx".format(file=name))
            os.startfile("D:\\Test\\Test File\\{file}.docx".format(file=name))
        elif "excel" in file_type or "trang tính" in file_type:
            speak("Bạn muốn đặt tên file là gì?")
            time.sleep(3)
            name = get_text()

            input_detail = [[]]
            output_excel_path = (
                "D:\\Test\\Test File\\{file}.xlsx").format(file=name)
            create_excel(input_detail, output_excel_path)
            speak("Đã tạo file. Dưới đây là đường dẫn tới file bạn vừa tạo.")
            time.sleep(5)
            print("Bot: D:\\Test\\Test File\\{file}.xlsx".format(file=name))
            os.startfile("D:\\Test\\Test File\\{file}.xlsx".format(file=name))
        elif "powerpoint" in file_type or "trình chiếu" in file_type:
            speak("Bạn muốn đặt tên file là gì?")
            time.sleep(3)
            name = get_text()
            file = open(
                "D:\\Test\\Test File\\{file}.pptx".format(file=name), "w")
            file.close()
            speak("Đã tạo file. Dưới đây là đường dẫn tới file bạn vừa tạo.")
            time.sleep(5)
            print("Bot: D:\\Test\\Test File\\{file}.pptx".format(file=name))
            os.startfile("D:\\Test\\Test File\\{file}.pptx".format(file=name))
        else:
            speak("Tạm thời tôi chưa thể tạo được loại file này hoặc tên loại file không chính xác. Xin hãy kiểm tra lại!")
            time.sleep(8)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# create_file()