# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import os
import time
from text_to_speech import speak
from get_text import get_text


# Mở các ứng dụng trên máy nếu có tồn tại.
def open_application():
    try:
        speak("Tên ứng dụng bạn muốn mở là gì?")
        time.sleep(3)
        text = get_text()
        if "google" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\Google Chrome.lnk"):
                speak("Mở Google Chrome.")
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Google Chrome")
            else:
                speak(
                    "Google Chrome chưa được cài đặt trên máy của bạn hoặc đường dẫn không chính xác. Vui lòng xem lại!")
                time.sleep(8)
        elif "văn bản" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\Word.lnk"):
                speak("Mở Microsoft Word.")
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Word")
            else:
                speak(
                    "Microsoft Word chưa được cài đặt trên máy của bạn hoặc đường dẫn không chính xác. Vui lòng xem lại!")
                time.sleep(8)
        elif "trang tính" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\Excel.lnk"):
                speak("Mở Microsoft Excel.")
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Excel")
            else:
                speak(
                    "Microsoft Excel chưa được cài đặt trên máy của bạn hoặc đường dẫn không chính xác. Vui lòng xem lại!")
                time.sleep(8)
        elif "trình chiếu" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\PowerPoint.lnk"):
                speak("Mở Microsoft PowerPoint.")
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\PowerPoint")
            else:
                speak(
                    "Microsoft PowerPoint chưa được cài đặt trên máy của bạn hoặc đường dẫn không chính xác. Vui lòng xem lại!")
                time.sleep(8)
        elif "bàn phím" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\UniKeyNT.lnk"):
                speak("Mở Unikey.")
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\UniKeyNT")
            else:
                speak(
                    "Unikey chưa được cài đặt trên máy của bạn hoặc đường dẫn không chính xác. Vui lòng xem lại!")
                time.sleep(8)
        elif "sổ tay" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\Notepad.lnk"):
                speak("Mở Notepad.")
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Notepad")
            else:
                speak("Có thể đường dẫn của bạn không chính xác. Vui lòng xem lại!")
                time.sleep(5)
        elif "thùng rác" in text or "recycle bin" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\Thùng rác.lnk"):
                speak("Mở Thùng rác.")
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Thùng rác")
            elif os.path.exists(f"D:\\Test\\Shortcut\\Recycle Bin.lnk"):
                speak("Mở Thùng rác.")
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Recycle Bin")
            else:
                speak("Có thể đường dẫn của bạn không chính xác. Vui lòng xem lại!")
                time.sleep(5)
        elif "vẽ" in text or "paint" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\Vẽ.lnk"):
                speak("Mở Paint.")
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Vẽ")
            elif os.path.exists(f"D:\\Test\\Shortcut\\Paint.lnk"):
                speak("Mở Paint.")
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Paint")
            else:
                speak("Có thể đường dẫn của bạn không chính xác. Vui lòng xem lại!")
                time.sleep(5)
        elif "máy tính" in text:
            if os.path.exists(f"C:\\Windows\\System32\\calc.exe"):
                speak("Mở máy tính.")
                time.sleep(2)
                os.startfile(f"C:\\Windows\\System32\\calc.exe")
            else:
                speak(
                    "Máy tính chưa được cài đặt trên máy của bạn hoặc đường dẫn không chính xác. Vui lòng xem lại!")
                time.sleep(8)
        elif "cmd" in text:
            if os.path.exists(f"C:\\Windows\\System32\\cmd.exe"):
                speak("Mở cmd.")
                time.sleep(2)
                os.startfile(f"C:\\Windows\\System32\\cmd.exe")
            else:
                speak("Có thể đường dẫn của bạn không chính xác. Vui lòng xem lại!")
                time.sleep(5)
        else:
            speak("Bạn có chắc chắn đã cài đặt ứng dụng này? Xin hãy kiểm tra lại!")
            time.sleep(5)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# open_application()