# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import pyqrcode
import os
from text_to_speech import speak


# Tạo mã qr code.
def create_qrcode():
    try:
        speak("Xin nhập đường dẫn cho mã qr của bạn!")
        time.sleep(3)
        input_data = input("Tôi: Mời nhập đường dẫn: ")
        path_split = input_data.split("//")[0]
        while "https:" != path_split and "http:" != path_split:
            print("Bot: Dường như đường dẫn của bạn không đúng. Xin mời nhập lại!")
            input_data = input("Tôi: Mời nhập đường dẫn: ")
            path_split = input_data.split("//")[0]
        qr = pyqrcode.create(input_data)
        qr.svg("D:\\Test\\Image\\qr_code.svg", scale=8)
        qr.png("D:\\Test\\Image\\qr_code.png", scale=8)
        speak("Đã tạo qr code. Phía dưới là đường dẫn tới ảnh qr vừa tạo.")
        print("Bot: D:\\Test\\Image\\qr_code.png")
        time.sleep(6)
        os.startfile("D:\\Test\\Image\\qr_code.png")
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# create_qrcode()