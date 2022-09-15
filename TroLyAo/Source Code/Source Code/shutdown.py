# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import os
from text_to_speech import speak
from get_text import get_text


# Tắt máy tính.
def shutdown():
    try:
        speak("Bạn có muốn tắt máy tính của mình không?")
        time.sleep(3)
        text = get_text()
        if "không" in text:
            return
        elif "có" in text:
            speak("Máy sẽ tắt sau 10 giây nữa.")
            os.system("shutdown /s /t 10")
            time.sleep(3)
        else:
            speak("Tôi không hiểu câu trả lời của bạn. Vui lòng thử lại sau!")
            time.sleep(5)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# shutdown()