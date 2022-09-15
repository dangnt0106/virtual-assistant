# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import urllib.request as urllib2
import json
import os
import ctypes
import time
from text_to_speech import speak


# Thay đổi hình nền máy tính ảnh lấy từ trên Internet.
def change_wallpaper_in_internet():
    try:
        api_key = "RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw"
        url = "https://api.unsplash.com/photos/random?client_id=" + api_key
        f = urllib2.urlopen(url)
        json_string = f.read()
        f.close()
        parsed_json = json.loads(json_string)
        photo = parsed_json["urls"]["full"]
        # Đường dẫn của mấy tấm ảnh nền mà mình muốn thay đổi.
        urllib2.urlretrieve(photo, f"D:\\Test\\Image\\background_test.jpg")
        image = os.path.join(f"D:\\Test\\Image\\background_test.jpg")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 3)
        speak("Hình nền máy tính vừa được thay đổi.")
        time.sleep(3)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# change_wallpaper_in_internet()