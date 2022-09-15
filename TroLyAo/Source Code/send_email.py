# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import smtplib
from text_to_speech import speak
from get_text import get_text


# Gửi email.
def send_email():
    speak("Hãy nhập tên đăng nhập email của bạn!")
    time.sleep(2)                                                            
    name = input("Tôi: Mời bạn nhập tên email đăng nhập: ")     # at9274229@gmail.com
    while "@" not in name:
        print("Bot: Tên email không hợp lệ, mời nhập lại.")
        name = input("Tôi: Mời bạn nhập tên email đăng nhập: ")
    speak("Hãy nhập mật khẩu email của bạn!")
    time.sleep(2)
    pasword = input("Tôi: Mời bạn nhập mật khẩu email: ")  # haha 123456

    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(name, pasword)
        speak("Hãy nhập tên email mà bạn muốn gửi!")
        time.sleep(2)
        name_send = input("Tôi: Mời bạn nhập tên email muốn gửi: ")
        while "@" not in name_send:
            print("Bot: Tên email không hợp lệ, mời nhập lại.")
            name_send = input("Tôi: Mời bạn nhập tên email muốn gửi: ")
        speak("Nội dung bạn muốn gửi là gì?")
        time.sleep(2)
        content = get_text()
        mail.sendmail(name, name_send, content.encode("utf-8"))
        mail.close()
        speak("Email của bạn vừa được gửi. Bạn kiểm tra lại email nhé.")
        time.sleep(7)
    except Exception as e:
        if smtplib.SMTPAuthenticationError:
            error = """
            Một trong các lỗi sau đã xảy ra:
            Có thể kí tự bạn nhập vào không hợp lệ.
            Có thể tên email và mật khẩu bạn nhập chưa chính xác. 
            Có thể email người nhận chưa chính xác.
            Có thể bạn chưa cấp quyền cho email của mình nên bị chặn.
            Bạn vui lòng kiểm tra lại lỗi bằng thông báo bên dưới!
            """
            speak(error)
            time.sleep(22)
            print("Bot: {ex}".format(ex=e))


# send_email()