# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import wikipedia
from text_to_speech import speak
from get_text import get_text

wikipedia.set_lang("vi")

# Kể chuyện.
def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ?")
        time.sleep(2)
        text = get_text()
        contents = wikipedia.summary(text).split("\n")
        speak(contents[0].split(".")[0])
        time.sleep(10)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không?")
            time.sleep(2)
            answer = get_text()
            if "có" not in answer:
                break
            speak(content)
            time.sleep(17)
        speak("Cảm ơn bạn đã lắng nghe!")
        time.sleep(3)
    except:
        speak("Tôi không định nghĩa được thuật ngữ của bạn. Xin mời bạn thử lại sau!")
        time.sleep(6)


#tell_me_about()