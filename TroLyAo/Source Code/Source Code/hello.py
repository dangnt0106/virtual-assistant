# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
from time import sleep, strftime
from text_to_speech import speak


# Chào hỏi. Tố Như sẽ phân vùng thời gian để chào cho hợp lý.
def hello(name):
    try:
        day_time = int(strftime("%H"))
        if 0 <= day_time < 4:
            speak(
                "Chào buổi khuya bạn {}. Bạn nên đi nghỉ ngơi đi nhé vì giờ đã khuya lắm rồi!".format(name))
        elif 4 <= day_time < 10:
            speak("Chào buổi sáng bạn {}. Chúc bạn một ngày mới tốt lành.".format(name))
        elif 10 <= day_time < 13:
            speak(
                "Chào buổi trưa bạn {}. Bạn nên nghỉ ngơi để có sức làm việc cho buổi chiều nhé!".format(name))
        elif 13 <= day_time < 18:
            speak(
                "Chào buổi chiều bạn {}. Chúc bạn có một buổi chiều thật năng động nhé.".format(name))
        elif 18 <= day_time < 21:
            speak(
                "Chào buổi tối bạn {}. Chúc bạn buổi tối thật vui vẻ bên gia đình nhé.".format(name))
        else:
            speak("Chào cuối ngày bạn {}. Bạn nhớ ngủ sớm để giữ gìn sức khỏe nha. Chúc bạn ngủ ngon.".format(name))
        time.sleep(10)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# hello("Mèo Con")