# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import os
import time
import ctypes
from text_to_speech import speak
from get_text import get_text


# Thay đổi hình nền được chọn từ máy tính.
def change_wallpaper_in_computer():
    try:
        speak("Bạn muốn chọn hình nào trong số những hình này để thay đổi hình nền?")
        os.startfile("D:\\Test\\Image")
        time.sleep(5)
        image = get_text()
        if os.path.exists("D:\\Test\\Image\\{image}.jpg".format(image=image)):
            path = "D:\\Test\\Image\\{image}.jpg".format(image=image)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
            speak("Hình nền máy tính vừa được thay đổi.")
            time.sleep(3)
        elif os.path.exists("D:\\Test\\Image\\{image}.png".format(image=image)):
            path = "D:\\Test\\Image\\{image}.png".format(image=image)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
            speak("Hình nền máy tính vừa được thay đổi.")
            time.sleep(3)
        else:
            speak("Có lẽ bạn đã phát âm sai tên của hình ảnh hoặc định dạng file không phù hợp. Vui lòng thử lại sau!")
            time.sleep(7.5)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


#change_wallpaper_in_computer()