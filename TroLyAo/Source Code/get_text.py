# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
from speech_to_text import get_audio
from text_to_speech import speak
from stop import stop_no_name


# Tố Như sẽ hỏi lại những gì mà bạn nói vào nhưng máy sẽ không nghe rõ do bị dính tạp âm.
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Tôi không nghe rõ. Bạn nói lại được không?")
            time.sleep(3)
    time.sleep(2)
    stop_no_name()
    return 0


# get_text()