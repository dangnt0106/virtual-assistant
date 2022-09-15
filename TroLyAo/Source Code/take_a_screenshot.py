# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import pyautogui
from PIL import Image
from text_to_speech import speak


# Chụp ảnh màn hình máy tính.
def take_a_screenshot():
    try:
        speak("Đã chụp ảnh. Dưới đây là đường dẫn của ảnh bạn vừa chụp.")
        print("Bot: D:\\Test\\Image\\screenshot.png")
        time.sleep(5)
        path = "D:\\Test\\Image\\screenshot.png"
        pyautogui.screenshot(path)
        im = Image.open(path)
        im.save(path)
        im.show(path)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


#take_a_screenshot()