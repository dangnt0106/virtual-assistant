# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import datetime
import playsound
from text_to_speech import speak
from get_text import get_text


# Cài báo thức.
def set_alarm():
    try:
        note = """
        Lưu ý là khi cài báo thức thì tôi sẽ không thể thực hiện bất kì hành động nào khác cho đến khi báo thức được reo. 
        Bạn cũng không nên tắt tôi đi nếu không báo thức sẽ không reo.
        Bạn có chắc chắn muốn cài báo thức không?
        """
        speak(note)
        time.sleep(17)  
        answer = get_text()
        if "có" in answer or "chắc chắn" in answer:
            speak("Mời bạn nhập giờ và phút cho báo thức?")
            time.sleep(3)
            alarmH = input("Tôi: Mời nhập giờ: ")
            while alarmH.isdigit() == False or 0 > int(alarmH) or int(alarmH) > 23:
                print("Bot: Nhập sai, mời nhập lại.")
                alarmH = input("Tôi: Mời nhập giờ: ")
            alarmM = input("Tôi: Mời nhập phút: ")
            while alarmM.isdigit() == False or 0 > int(alarmM) or int(alarmM) > 59:
                print("Bot: Nhập sai, mời nhập lại.")
                alarmM = input("Tôi: Mời nhập phút: ")
            speak("Báo thức sẽ là ban ngày (am) hay từ chiều đến đêm (pm)?")
            time.sleep(4)
            am_or_pm = (input("Tôi: Mời chọn am hay pm: "))
            while str(am_or_pm) != "am" and str(am_or_pm) != "pm":
                print("Bot: Nhập sai, mời nhập lại.")
                am_or_pm = input("Tôi: Mời chọn am hay pm: ")
            if "pm" == am_or_pm:
                alarmH = int(alarmH) + 12
                print("Bot: Đang chờ báo thức: {hour} giờ {minute} phút pm... ".format(
                    hour=alarmH, minute=alarmM))
            elif "am" == am_or_pm:
                print("Bot: Đang chờ báo thức: {hour} giờ {minute} phút am... ".format(
                    hour=alarmH, minute=alarmM))
                pass
            else:
                speak("Bạn đã không chọn đúng giá trị am hay pm. Vui lòng thử lại sau!")
                time.sleep(7)
                return
            while(1 == 1):
                if int(alarmH) == datetime.datetime.now().hour and int(alarmM) == datetime.datetime.now().minute:
                    speak("Đã tới giờ báo thức!")
                    time.sleep(2)
                    playsound.playsound("D:\\Test\\Sound\\alarm.mp3")
                    time.sleep(17)
                    return
        elif "không" in answer:
            return
        else:
            speak(
                "Tôi không hiểu câu trả lời của bạn hoặc có thể bạn đã phát âm không rõ. Vui lòng thử lại sau!")
            time.sleep(7)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# set_alarm()