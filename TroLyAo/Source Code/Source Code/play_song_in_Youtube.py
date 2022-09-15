# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import webbrowser
from text_to_speech import speak
from get_text import get_text
from youtube_search import YoutubeSearch


# Tìm kiếm và phát nhạc trên Youtube.
def play_song_in_Youtube():
    try:
        speak("Xin mời bạn chọn tên bài hát!")
        time.sleep(2)
        mysong = get_text()
        while True:
            result = YoutubeSearch(mysong, max_results=10).to_dict()
            if result:
                break
            else:
                speak(
                    "Bài hát bạn muốn tìm không có trên Youtube hoặc tiêu đề không chính xác. Xin mời bạn kiểm tra lại!")
                time.sleep(8)
                return
        url = "https://www.youtube.com" + result[0]["url_suffix"]
        webbrowser.open(url)
        speak("Bài hát bạn yêu cầu đã được mở.")
        time.sleep(3)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# play_song_in_Youtube()