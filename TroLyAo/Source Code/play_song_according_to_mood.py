# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import random
import os
import webbrowser
from text_to_speech import speak
from get_text import get_text


# Nghe nhạc theo tâm trạng.
def play_song_according_to_mood():
    try:
        speak("Bây giờ tâm trạng của bạn như thế nào?")
        time.sleep(3)
        mood = get_text()
        if "vui" in mood:
            basedir = "D:\\Test\\Music\\Happy\\"
            file = random.choice([x for x in os.listdir(
                basedir) if os.path.isfile(os.path.join(basedir, x))])
            webbrowser.open(os.path.join(basedir, file))
            speak("Một bài hát vui nhộn vừa được mở.")
            time.sleep(3)
        elif "buồn" in mood:
            basedir = "D:\\Test\\Music\\Sad\\"
            file = random.choice([x for x in os.listdir(
                basedir) if os.path.isfile(os.path.join(basedir, x))])
            webbrowser.open(os.path.join(basedir, file))
            speak("Một bài hát buồn vừa được mở.")
            time.sleep(3)
        elif "chán" in mood:
            basedir = "D:\\Test\\Music\\Bored\\"
            file = random.choice([x for x in os.listdir(
                basedir) if os.path.isfile(os.path.join(basedir, x))])
            webbrowser.open(os.path.join(basedir, file))
            speak("Một bài hát giúp bạn thư giản vừa được mở.")
            time.sleep(3)
        else:
            speak(
                "Tôi không hiểu tâm trạng này của bạn hoặc cảm xúc này chưa có bài hát nào để phát.")
            time.sleep(6)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# play_song_according_to_mood()