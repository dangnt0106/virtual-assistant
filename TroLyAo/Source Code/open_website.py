# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import re
import webbrowser
import time
from text_to_speech import speak


# Tố Như mở web lên.
def open_website(text):
    try:
        reg_ex = re.search("mở (.+)", text)
        if reg_ex:
            domain = reg_ex.group(1)
            if "com" in text:
                url = "https://www." + domain
                webbrowser.open(url)
                speak("Trang web bạn yêu cầu đã được mở.")
                time.sleep(3)
                return True
            else:
                url = "https://www." + domain + ".com"
                webbrowser.open(url)
                speak("Trang web bạn yêu cầu đã được mở.")
                time.sleep(3)
                return True
        else:
            return False
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# open_website("mở youtube")
# open_website("mở youtube.com")