# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import datetime
import time
from text_to_speech import speak

# Tố Như sẽ trả lời về thời gian và ngày tháng.
def get_time(text):
    try:
        now = datetime.datetime.now()
        if "giờ" in text:
            speak("Bây giờ là %d giờ %d phút %d giây." %
                  (now.hour, now.minute, now.second))
        elif "ngày" in text:
            speak("Hôm nay là ngày %d tháng %d năm %d." %
                  (now.day, now.month, now.year))
        else:
            speak("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
        time.sleep(5)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# get_time("giờ")
# get_time("ngày")