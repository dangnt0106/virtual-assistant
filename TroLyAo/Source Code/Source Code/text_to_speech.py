# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import os
import playsound
from gtts import gTTS

language = "vi"

# Text - to - speech: Chuyển đổi văn bản thành giọng nói.
def speak(text):
    try:
        print("Bot: {}".format(text))
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3", False)
        os.remove("sound.mp3")
    except:
        print("Bot: Đã xảy ra lỗi. Vui lòng thử lại sau!")


# speak()