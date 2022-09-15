# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import os
from text_to_speech import speak
from get_text import get_text


# Chơi game.
def play_game():
    try:
        speak("Bạn muốn chơi game nào nhỉ?")
        time.sleep(2)
        game = get_text().title()
        if os.path.exists(f"D:\\Test\\Game\\{game}.exe"):
            os.startfile(f"D:\\Test\\Game\\{game}.exe")
            speak("Game {} đã được mở.".format(game))
            time.sleep(2)
        else:
            speak(
                "Game bạn yêu cầu chưa có trong máy hoặc sai đường dẫn. Bạn hãy kiểm tra lại nhé!")
            time.sleep(6)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# play_game()