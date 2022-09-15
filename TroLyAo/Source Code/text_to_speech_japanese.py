# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import playsound
import os
import time
from gtts import gTTS
from text_to_speech import speak

language2 = "ja"

# Text - to - speech: Chuyển đổi văn bản thành giọng nói tiếng Nhật.
def speak_japanese(text):
    try:
        print("Bot: {}".format(text))
        tts = gTTS(text=text, lang=language2, slow=False)
        tts.save("sound_japanese.mp3")
        playsound.playsound("sound_japanese.mp3", False)
        os.remove("sound_japanese.mp3")
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)

# speak_japanese()