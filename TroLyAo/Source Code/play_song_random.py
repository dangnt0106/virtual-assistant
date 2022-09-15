# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import random
import os
import webbrowser
import time
from text_to_speech import speak


# Nghe một bài át ngẫu nhiên.
def play_song_random():
    try:
        basedir = "D:\\Test\\Music\\"
        file = random.choice([x for x in os.listdir(
            basedir) if os.path.isfile(os.path.join(basedir, x))])
        webbrowser.open(os.path.join(basedir, file))
        speak("Một bài hát bất kì vừa được mở.")
        time.sleep(3)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# play_song_random()