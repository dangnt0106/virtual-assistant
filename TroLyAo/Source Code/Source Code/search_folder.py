# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import os
import shutil
from text_to_speech import speak
from get_text import get_text


# Tìm thư mục trên máy tính.
def search_folder():
    try:
        speak("Xin hãy nhập ổ đĩa bạn muốn tìm thư mục!")
        time.sleep(3)
        disk = str(input("Tôi: Mời nhập tên ổ đĩa: ")).upper()
        while disk != "C" and disk != "D":
            print("Bot: Nhập sai, mời nhập lại. Lưu ý hiện giờ tôi chỉ có thể tìm kiếm trên hai ổ đĩa C và D mà thôi.")
            disk = str(input("Tôi: Mời nhập tên ổ đĩa: ")).upper()
        speak("Xin hãy nhập tên thư mục bạn muốn tìm kiếm!")
        time.sleep(4)
        name = input("Tôi: Nhập tên thư mục muốn tìm: ")
        count = 0
        list_folder = []
        print("Bot: Bạn vui lòng đợi trong giây lát. Đang tiến hành tìm kiếm...")
        for root, dirs, files in os.walk(f"{disk}:\\".format(disk=disk)):
            if name in dirs:
                f = os.path.join(root, name)
                list_folder.append(f)
                count = count + 1
        if count == 1:
            speak("Tìm thấy thành công thư mục " + name +
                  ". Dưới đây là đường dẫn của thư mục.")
            time.sleep(7.5)
            print("Bot: " + f)
            speak(
                "Bạn có muốn thực hiện thao tác nào khác với thư mục vừa tìm được không?")
            time.sleep(5)
            action = get_text()
            if "không" in action:
                return
            elif "mở" in action or "bật" in action:
                speak("Đã mở thư mục.")
                time.sleep(2)
                os.startfile(f)
            elif "đổi tên" in action or "thay tên" in action:
                speak("Tên mà bạn muốn đổi là gì vậy?")
                time.sleep(3)
                new_name = get_text()
                cut_name = name
                path = f.rstrip(cut_name)
                os.rename(f, path + new_name)
                speak("Đã đổi tên thư mục.")
                print("Bot: Đường dẫn mới của thư mục sau khi đổi tên ",
                      path + new_name)
                time.sleep(2)
            elif "xóa" in action:
                speak("Bạn có chắc chắn muốn xóa thư mục này không?")
                time.sleep(4)
                answer = get_text()
                if "có" in answer or "chắc chắn" in answer:
                    for dirpath, dirnames, files in os.walk(f):
                        if os.listdir(dirpath) == []:
                            os.rmdir(f)
                        else:
                            shutil.rmtree(f)
                    speak("Đã xóa thư mục.")
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
            speak("Tìm thấy thành công {count} thư mục tên {name}. Dưới đây là đường dẫn của các thư mục đó.".format(
                count=count, name=name))
            for i in list_folder:
                print("Bot: ", i)
            time.sleep(7.5)
            speak("Bạn có muốn mở các thư mục này không?")
            time.sleep(3)
            text = get_text()
            if "không" in text:
                return
            elif "có" in text or "ok" in text:
                speak("Đã mở các thư mục.")
                time.sleep(2)
                for i in list_folder:
                    os.startfile(i)
            else:
                speak("Tôi chưa hiểu ý của bạn.")
                time.sleep(3)
        else:
            speak("Tôi không tìm thấy thư mục này.")
            time.sleep(3)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# search_folder()