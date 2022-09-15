# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import os
from text_to_speech import speak
from get_text import get_text
from youtube_search import YoutubeSearch
from pytube import YouTube


# Tải video trên youtube về máy tính.
def download_video_Youtube():
    try:
        speak("Video bạn muốn tải tên là gì nhỉ?")
        time.sleep(3)
        video = get_text()
        while True:
            result = YoutubeSearch(video, max_results=10).to_dict()
            if result:
                break
            else:
                speak(
                    "Video bạn muốn tải không có trên Youtube hoặc tiêu đề không chính xác. Xin mời bạn kiểm tra lại!")
                time.sleep(8)
                return
        print("Bot: Bạn vui lòng đợi trong giây lát. Đang tiến hành tải video...")
        url = "https://www.youtube.com" + result[0]["url_suffix"]
        file = YouTube(url).streams.filter(progressive=True, file_extension="mp4").last(
        ).download(output_path="D:\\Test\\Video\\")
        print("Bot: Đường dẫn video vừa tải " + file)
        if os.path.exists(file):
            speak('Đã tải xong video "{video}".'.format(video=video.title()))
            time.sleep(4)
            speak("Bạn có muốn mở video lên không?")
            time.sleep(3)
            text = get_text()
            if "có" in text:
                speak("Đã mở video.")
                time.sleep(2)
                os.startfile(file)
            else:
                return
        else:
            speak("Tải video không thành công. Bạn hãy kiểm tra lại nhé.")
            time.sleep(5)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# download_video_Youtube()