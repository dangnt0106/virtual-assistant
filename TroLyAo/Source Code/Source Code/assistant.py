# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
from text_to_speech import speak
from get_text import get_text
from stop import stop
from help_me import help_me
from hello import hello
from get_time import get_time
from open_google_and_search import open_google_and_search
from open_website import open_website
from open_application import open_application
from send_email import send_email
from current_weather import current_weather
from play_song_in_Youtube import play_song_in_Youtube
from change_wallpaper_in_internet import change_wallpaper_in_internet
from change_wallpaper_in_computer import change_wallpaper_in_computer
from read_news import read_news
from tell_me_about import tell_me_about
from introduce import introduce
from open_google_and_search_image import open_google_and_search_image
from play_song_random import play_song_random
from play_song_in_computer import play_song_in_computer
from play_song_according_to_mood import play_song_according_to_mood
from search_file import search_file
from play_game import play_game
from update_covid_19 import update_covid_19
from update_gold_price import update_gold_price
from take_a_screenshot import take_a_screenshot
from translate import translate
from download_video_Youtube import download_video_Youtube
from create_file import create_file
from create_folder import create_folder
from search_folder import search_folder
from set_alarm import set_alarm
from create_qrcode import create_qrcode
from shutdown import shutdown


# Liên kết các hàm lại để tạo thành trợ lí .
def assistant():
    try:
        speak("Xin chào, bạn tên là gì nhỉ?")
        time.sleep(1.5)
        name = get_text().title()
        if name:
            speak("Chào bạn {}.".format(name))
            time.sleep(2)
            speak("Bạn cần tôi giúp đỡ gì ạ?")
            time.sleep(3)
            while True:
                text = get_text()
                if not text:
                    break
                elif "dừng chương trình" in text or "không cần" in text or "tạm biệt" in text or "kết thúc" in text or "chào robot" in text or "ngủ thôi" in text:
                    stop(name)
                    break
                elif "có thể làm gì" in text:
                    help_me()
                elif "chào" in text:
                    hello(name)
                elif "xem giờ" in text or "ngày" in text:
                    get_time(text)
                elif "mở google và tìm kiếm" in text:
                    open_google_and_search()
                elif "mở " in text:
                    open_website(text)
                elif "ứng dụng" in text:
                    open_application()
                elif "email" in text or "mail" in text or "gmail" in text:
                    send_email()
                elif "thời tiết" in text:
                    current_weather()
                elif "nghe nhạc trên youtube" in text:
                    play_song_in_Youtube()
                elif "hình nền" in text:
                    speak("Bạn muốn lấy hình ngẫu nhiên trên mạng hay hình trên máy tính?")
                    time.sleep(5)
                    option = get_text()
                    if "trên mạng" in option:
                        change_wallpaper_in_internet()
                    elif "trên máy tính" in option:
                        change_wallpaper_in_computer()
                    else:
                        speak("Tôi chưa hiểu ý của bạn.")
                        time.sleep(3)
                elif "đọc báo" in text:
                    read_news()
                elif "định nghĩa" in text:
                    tell_me_about()
                elif "giới thiệu" in text:
                    introduce()
                elif "tìm hình ảnh về" in text:
                    open_google_and_search_image(text)
                elif "nghe nhạc trên máy tính" in text:
                    speak(
                        "Bạn muốn nghe một bài hát ngẫu nhiên hay chỉ định một bài hát cụ thể?")
                    time.sleep(5)
                    option = get_text()
                    if "ngẫu nhiên" in option:
                        play_song_random()
                    elif "cụ thể" in option:
                        play_song_in_computer()
                    else:
                        speak("Tôi chưa hiểu ý của bạn.")
                        time.sleep(3)
                elif "nghe nhạc theo tâm trạng" in text:
                    play_song_according_to_mood()
                elif "tìm tập tin" in text or "tìm file" in text:
                    search_file()
                elif "game" in text or "trò chơi" in text:
                    play_game()
                elif "dịch bệnh" in text:
                    update_covid_19()
                elif "giá vàng" in text:
                    a = update_gold_price()
                    b = a["golds"]
                    c = b[0]
                    d = c["value"]
                    speak(
                        "Dưới đây là bảng danh sách mới nhất của giá vàng trên thị trường.")
                    time.sleep(5)
                    for i in d:
                        print(
                            "\t|---------------------------------------------------------------------------------------------------------------------------------------|")
                        print("\t Giá mua:  {0}   Giá bán:  {1}   Loại vàng:  {2}   Cập nhật lúc {3} tại {4}.".format(
                            i["buy"], i["sell"], i["type"], i["updated"], i["brand"]))
                        print(
                            "\t|---------------------------------------------------------------------------------------------------------------------------------------|")
                elif "chụp ảnh màn hình" in text:
                    take_a_screenshot()
                elif "dịch thuật" in text:
                    translate()
                elif "tải video youtube" in text:
                    download_video_Youtube()
                elif "tạo file" in text or "tạo tập tin" in text:
                    create_file()
                elif "tạo thư mục" in text or "tạo folder" in text:
                    create_folder()
                elif "tìm thư mục" in text:
                    search_folder()
                elif "báo thức" in text:
                    set_alarm()
                elif "qr code" in text or "tạo mã qr" in text:
                    create_qrcode()
                elif "tắt máy" in text or "shutdown" in text:
                    shutdown()
                else:
                    speak("Bạn cần tôi giúp gì ạ?")
                    time.sleep(2)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# assistant()