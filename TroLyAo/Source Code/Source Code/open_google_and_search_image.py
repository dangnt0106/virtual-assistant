# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from text_to_speech import speak

path = ChromeDriverManager().install()

# Tìm kiếm hình ảnh trên Google.
def open_google_and_search_image(text):
    try:
        search_for = text.split("về", 1)[1]
        speak("Vâng thưa sếp!")
        driver = webdriver.Chrome(path)
        driver.get("https://images.google.com")
        que = driver.find_element_by_xpath("//input[@name='q']")
        que.send_keys(str(search_for))
        que.send_keys(Keys.RETURN)
        speak("Đây là những hình ảnh bạn cần tìm.")
        time.sleep(4)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# open_google_and_search_image("về mèo con")