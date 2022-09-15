# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import os
from text_to_speech import speak
from get_text import get_text


# Tìm kiếm và phát nhạc trên máy tính.
def play_song_in_computer():
    try:
        speak("Bạn muốn nghe bài hát nào?")
        time.sleep(2)
        mysong = get_text()
        if os.path.exists(f"D:\\Test\\Music\\{mysong}.mp3"):
            os.startfile(f"D:\\Test\\Music\\{mysong}.mp3")
            speak("Bài hát bạn yêu cầu đã được mở.")
            time.sleep(3)
        elif os.path.exists(f"D:\\Test\\Music\\{mysong}.wav"):
            os.startfile(f"D:\\Test\\Music\\{mysong}.wav")
            speak("Bài hát bạn yêu cầu đã được mở.")
            time.sleep(3)
        elif os.path.exists(f"D:\\Test\\Music\\{mysong}.wma"):
            os.startfile(f"D:\\Test\\Music\\{mysong}.wma")
            speak("Bài hát bạn yêu cầu đã được mở.")
            time.sleep(3)
        else:
            speak("Bài hát bạn yêu cầu chưa có trong máy hoặc sai tên. Bạn hãy tải bài hát hoặc kiểm tra lại tên bài hát!")
            time.sleep(8)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# play_song_in_computer()