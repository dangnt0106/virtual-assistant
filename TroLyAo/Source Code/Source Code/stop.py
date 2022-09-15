# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
from enum import unique
import time
from time import sleep, strftime
from text_to_speech import speak


# Tố Như sẽ chào tạm biệt bạn khi bạn tạm biệt cô ấy.
def stop(name):
    try:
        day_time = int(strftime("%H"))
        if 0 <= day_time < 4:
            speak(
                "Hẹn gặp lại bạn {} sau!. Bạn nên đi nghỉ ngơi đi nhé vì giờ đã khuya lắm rồi!".format(name))
        elif 4 <= day_time < 10:
            speak("Hẹn gặp lại bạn {} sau!. Chúc bạn một ngày mới tốt lành.".format(name))
        elif 10 <= day_time < 13:
            speak(
                "Hẹn gặp lại bạn {} sau!. Bạn nên nghỉ ngơi để có sức làm việc cho buổi chiều nhé!".format(name))
        elif 13 <= day_time < 18:
            speak(
                "Hẹn gặp lại bạn {} sau!. Chúc bạn có một buổi chiều thật vui vẻ.".format(name))
        elif 18 <= day_time < 21:
            speak(
                "Hẹn gặp lại bạn {} sau!. Chúc bạn buổi tối thật vui vẻ nhé.".format(name))
        else:
            speak("Hẹn gặp lại bạn {} sau!. Bạn nhớ ngủ sớm để giữ gìn sức khỏe nha. Chúc bạn ngủ ngon.".format(name))
        time.sleep(10)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# stop("Mèo Con")


# Chào tạm biệt khi AI không nghe rõ trong 3 lần.
def stop_no_name():
    speak("Hẹn gặp lại bạn sau!")
    time.sleep(2)


# stop_no_name()