# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import speech_recognition as sr


# Speech - to - text: Chuyển đổi giọng nói bạn yêu cầu vào thành văn bản hiện ra khi máy trả lại kết quả đã nghe.
def get_audio():
    print("\nBot: \tĐang nghe \t |--__--| \n")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end="")
        audio = r.listen(source, phrase_time_limit=8)
    try:
        text = r.recognize_google(audio, language="vi-VN")
        print(text)
        return text.lower()
    except:
        print("...")
        return 0


# get_audio()