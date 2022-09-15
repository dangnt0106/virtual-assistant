# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import webbrowser
from text_to_speech import speak
from get_text import get_text


# Mở và tìm kiếm từ khóa trên Google.
def open_google_and_search():
    try:
        speak("Bạn muốn tìm kiếm gì vậy?")
        time.sleep(3)
        search = str(get_text()).lower()
        url = f"https://www.google.com/search?q={search}"
        webbrowser.get().open(url)
        speak("Đây là thông tin bạn cần tìm.")
        time.sleep(3)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# open_google_and_search()