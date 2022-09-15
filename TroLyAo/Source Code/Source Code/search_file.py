# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import os
from text_to_speech import speak
from get_text import get_text


# Tìm file trên máy tính.
def search_file():
    try:
        speak("Xin hãy nhập ổ đĩa bạn muốn tìm file!")
        time.sleep(3)
        disk = str(input("Tôi: Mời nhập tên ổ đĩa: ")).upper()
        while disk != "C" and disk != "D":
            print("Bot: Nhập sai, mời nhập lại. Lưu ý hiện giờ tôi chỉ có thể tìm kiếm trên hai ổ đĩa C và D mà thôi.")
            disk = str(input("Tôi: Mời nhập tên ổ đĩa: ")).upper()
        speak("Xin hãy nhập tên file bạn muốn tìm kiếm! Lưu ý hãy nhập cả đuôi file.")
        time.sleep(5)
        name = input("Tôi: Nhập tên file muốn tìm: ")
        count = 0
        list_file = []
        print("Bot: Bạn vui lòng đợi trong giây lát. Đang tiến hành tìm kiếm...")
        for root, dirs, files in os.walk(f"{disk}:\\".format(disk=disk)):
            if name in files:
                f = os.path.join(root, name)
                list_file.append(f)
                count = count + 1
        if count == 1:
            speak("Tìm thấy thành công file " + name +
                  ". Dưới đây là đường dẫn của file.")
            time.sleep(7.5)
            print("Bot: " + f)
            speak("Bạn có muốn thực hiện thao tác nào khác với file vừa tìm được không?")
            time.sleep(5)
            action = get_text()
            if "không" in action:
                return
            elif "mở" in action or "bật" in action:
                speak("Đã mở file.")
                time.sleep(2)
                os.startfile(f)
            elif "đổi tên" in action or "thay tên" in action:
                speak("Tên mà bạn muốn đổi là gì vậy?")
                time.sleep(3)
                new_name = get_text()
                cut_name = name
                path = f.rstrip(cut_name)
                file_extension = name.rsplit(".")[-1]
                os.rename(f, path + new_name + "." + file_extension)
                speak("Đã đổi tên file.")
                print("Bot: Đường dẫn mới của file sau khi đổi tên ",
                      path + new_name + "." + file_extension)
                time.sleep(2)
            elif "xóa" in action:
                speak("Bạn có chắc chắn muốn xóa file này không?")
                time.sleep(4)
                answer = get_text()
                if "có" in answer or "chắc chắn" in answer:
                    os.remove(f)
                    speak("Đã xóa file.")
                    time.sleep(2)
                elif "không" in answer:
                    return
                else:
                    speak("Tôi chưa hiểu ý của bạn.")
                    time.sleep(3)
            else:
                speak("Tôi chưa hiểu ý của bạn.")
                time.sleep(3)
        elif count > 1:
            speak("Tìm thấy thành công {count} file tên {name}. Dưới đây là đường dẫn của các file đó.".format(
                count=count, name=name))
            for i in list_file:
                print("Bot: ", i)
            time.sleep(7.5)
            speak("Bạn có muốn mở các file này không?")
            time.sleep(3)
            text = get_text()
            if "không" in text:
                return
            elif "có" in text or "ok" in text:
                speak("Đã mở các file.")
                time.sleep(2)
                for i in list_file:
                    os.startfile(i)
            else:
                speak("Tôi chưa hiểu ý của bạn.")
                time.sleep(3)
        else:
            speak("Tôi không tìm thấy file này.")
            time.sleep(3)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# search_file()