# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import os
from text_to_speech import speak
from get_text import get_text


# Tạo thư mục cho máy tính. Ở đây set cứng đường dẫn luôn.
def create_folder():
    try:
        speak("Bạn muốn tạo thư mục tên gì?")
        time.sleep(2)
        text = get_text()
        dirname = "D:\\Test\\Test Folder\\" + text
        if os.path.isdir("D:\\Test\\Test Folder\\" + text) == True:
            speak(
                "Tên thư mục đã được sử dụng cho một thư mục khác. Vui lòng thử lại sau!")
            time.sleep(6)
            return
        else:
            os.mkdir(dirname)
    except OSError:
        speak("Tạo thư mục không thành công. Vui lòng kiểm tra lại.")
        time.sleep(4)
    else:
        speak("Tạo thư mục thành công. Dưới đây là tên đường dẫn tới thư mục bạn vừa tạo.")
        time.sleep(6)
        os.startfile("D:\\Test\\Test Folder\\" + text)
        print("Bot: " + dirname)


# create_folder()