# Import các thư viện cần thiết cho quá trình tạo nên trợ lí ảo.
import os
import random
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import openpyxl
import pyautogui
import shutil
import pyqrcode
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep, strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from PIL import Image
from googletrans import Translator
from pytube import YouTube
from docx import Document


# Khai báo các biến cho quá trình làm trợ lí ảo Tố Như.
wikipedia.set_lang("vi")
language = "vi"
path = ChromeDriverManager().install()


# Text - to - speech: Chuyển đổi văn bản thành giọng nói.
def speak(text):
    try:
        print("Bot: {}".format(text))
        tts = gTTS(text = text, lang = language, slow = False)
        tts.save("sound.mp3")
        playsound.playsound("sound.mp3", False)
        os.remove("sound.mp3")
    except:
        print("Bot: Đã xảy ra lỗi. Vui lòng thử lại sau!")
#speak()


# Speech - to - text: Chuyển đổi giọng nói bạn yêu cầu vào thành văn bản hiện ra khi máy trả lại kết quả đã nghe.
def get_audio():
    print("\nBot: \tĐang nghe \t |--__--| \n")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end = "")
        audio = r.listen(source, phrase_time_limit = 8)
        try:
            text = r.recognize_google(audio, language = "vi-VN")
            print(text)
            return text.lower()
        except:
            print("...")
            return 0
#get_audio()


# Tố Như sẽ chào tạm biệt bạn khi bạn tạm biệt cô ấy.
def stop(name):
    try:
        day_time = int(strftime("%H"))
        if 0 <= day_time < 4:
            speak("Hẹn gặp lại bạn {} sau!. Bạn nên đi nghỉ ngơi đi nhé vì giờ đã khuya lắm rồi!".format(name))
        elif 4 <= day_time < 10:
            speak("Hẹn gặp lại bạn {} sau!. Chúc bạn một ngày mới tốt lành.".format(name))
        elif 10 <= day_time < 13:
            speak("Hẹn gặp lại bạn {} sau!. Bạn nên nghỉ ngơi để có sức làm việc cho buổi chiều nhé!".format(name))
        elif 13 <= day_time < 18:
            speak("Hẹn gặp lại bạn {} sau!. Chúc bạn có một buổi chiều thật vui vẻ.".format(name))
        elif 18 <= day_time < 21:
            speak("Hẹn gặp lại bạn {} sau!. Chúc bạn buổi tối thật vui vẻ nhé.".format(name))
        else:
            speak("Hẹn gặp lại bạn {} sau!. Bạn nhớ ngủ sớm để giữ gìn sức khỏe nha. Chúc bạn ngủ ngon.".format(name))
        time.sleep(10)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#stop()


# Chào tạm biệt khi AI không nghe rõ trong 3 lần.
def stop_no_name():
    speak("Hẹn gặp lại bạn sau!")
    time.sleep(2)
#stop_no_name()


# Tố Như sẽ hỏi lại những gì mà bạn nói vào nhưng máy sẽ không nghe rõ do bị dính tạp âm.
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Tôi không nghe rõ. Bạn nói lại được không?")
            time.sleep(3)
    time.sleep(2)
    stop_no_name()
    return 0
#get_text()


# Chào hỏi. Tố Như sẽ phân vùng thời gian để chào cho hợp lý.
def hello(name):
    try:
        day_time = int(strftime("%H"))
        if 0 <= day_time < 4:
            speak("Chào buổi khuya bạn {}. Bạn nên đi nghỉ ngơi đi nhé vì giờ đã khuya lắm rồi!".format(name))
        elif 4 <= day_time < 10:
            speak("Chào buổi sáng bạn {}. Chúc bạn một ngày mới tốt lành.".format(name))
        elif 10 <= day_time < 13:
            speak("Chào buổi trưa bạn {}. Bạn nên nghỉ ngơi để có sức làm việc cho buổi chiều nhé!".format(name))
        elif 13 <= day_time < 18:
            speak("Chào buổi chiều bạn {}. Chúc bạn có một buổi chiều thật năng động nhé.".format(name))
        elif 18 <= day_time < 21:
            speak("Chào buổi tối bạn {}. Chúc bạn buổi tối thật vui vẻ bên gia đình nhé.".format(name))
        else:
            speak("Chào cuối ngày bạn {}. Bạn nhớ ngủ sớm để giữ gìn sức khỏe nha. Chúc bạn ngủ ngon.".format(name))
        time.sleep(10)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#hello()


# Tố Như sẽ trả lời về thời gian và ngày tháng.
def get_time(text):
    try:
        now = datetime.datetime.now()
        if "giờ" in text:
            speak("Bây giờ là %d giờ %d phút %d giây." % (now.hour, now.minute, now.second))
        elif "ngày" in text:
            speak("Hôm nay là ngày %d tháng %d năm %d." %
                (now.day, now.month, now.year))
        else:
            speak("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
        time.sleep(4)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#get_time()


# Mở các ứng dụng trên máy nếu có tồn tại.
def open_application():
    try:
        speak("Tên ứng dụng bạn muốn mở là gì?")
        time.sleep(3)
        text = get_text()
        if "google" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\Google Chrome.lnk"):
                speak("Mở Google Chrome")
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Google Chrome") # Trong ngoặc là đường dẫn đến ứng dụng trong máy
            else:
                speak("Google Chrome chưa được cài đặt trên máy của bạn hoặc đường dẫn không chính xác. Vui lòng xem lại!")
                time.sleep(8)    
        elif "văn bản" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\Word.lnk"):
                speak("Mở Microsoft Word") 
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Word")
            else:
                speak("Microsoft Word chưa được cài đặt trên máy của bạn hoặc đường dẫn không chính xác. Vui lòng xem lại!")
                time.sleep(8)     
        elif "trang tính" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\Excel.lnk"):
                speak("Mở Microsoft Excel")
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Excel")
            else:
                speak("Microsoft Excel chưa được cài đặt trên máy của bạn hoặc đường dẫn không chính xác. Vui lòng xem lại!")
                time.sleep(8)     
        elif "trình chiếu" in text: 
            if os.path.exists(f"D:\\Test\\Shortcut\\PowerPoint.lnk"): 
                speak("Mở Microsoft PowerPoint") 
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\PowerPoint")
            else:
                speak("Microsoft PowerPoint chưa được cài đặt trên máy của bạn hoặc đường dẫn không chính xác. Vui lòng xem lại!")
                time.sleep(8)      
        elif "bàn phím" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\UniKeyNT.lnk"):   
                speak("Mở Unikey") 
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\UniKeyNT")
            else:
                speak("Unikey chưa được cài đặt trên máy của bạn hoặc đường dẫn không chính xác. Vui lòng xem lại!")
                time.sleep(8)
        elif "sổ tay" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\Notepad.lnk"):
                speak("Mở Notepad") 
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Notepad")
            else:
                speak("Có thể đường dẫn của bạn không chính xác. Vui lòng xem lại!")
                time.sleep(5)
        elif "thùng rác" in text or "recycle bin" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\Thùng rác.lnk"):
                speak("Mở Thùng rác") 
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Thùng rác")
            elif os.path.exists(f"D:\\Test\\Shortcut\\Recycle Bin.lnk"):
                speak("Mở Thùng rác") 
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Recycle Bin")
            else:
                speak("Có thể đường dẫn của bạn không chính xác. Vui lòng xem lại!")
                time.sleep(5)
        elif "vẽ" in text or "paint" in text:
            if os.path.exists(f"D:\\Test\\Shortcut\\Vẽ.lnk"):
                speak("Mở Paint") 
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Vẽ")
            elif os.path.exists(f"D:\\Test\\Shortcut\\Paint.lnk"):
                speak("Mở Paint") 
                time.sleep(2)
                os.startfile(f"D:\\Test\\Shortcut\\Paint")
            else:
                speak("Có thể đường dẫn của bạn không chính xác. Vui lòng xem lại!")
                time.sleep(5)    
        elif "máy tính" in text:
            if os.path.exists(f"C:\\Windows\\System32\\calc.exe"):
                speak("Mở máy tính") 
                time.sleep(2)
                os.startfile(f"C:\\Windows\\System32\\calc.exe")        
            else:
                speak("Máy tính chưa được cài đặt trên máy của bạn hoặc đường dẫn không chính xác. Vui lòng xem lại!")
                time.sleep(8)
        elif "cmd" in text:
            if os.path.exists(f"C:\\Windows\\System32\\cmd.exe"):
                speak("Mở cmd") 
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
#open_application()


# Tố Như mở web lên.
def open_website(text):
    try:
        reg_ex = re.search("mở (.+)", text)
        if reg_ex:
            domain = reg_ex.group(1)
            if "com" in text:
                url = "https://www." + domain
                webbrowser.open(url)
                speak("Trang web bạn yêu cầu đã được mở.")
                time.sleep(3)
                return True
            else:
                url = "https://www." + domain + ".com"
                webbrowser.open(url)
                speak("Trang web bạn yêu cầu đã được mở.")
                time.sleep(3)
                return True
        else:
            return False
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#open_website()


# Mở và tìm kiếm từ khóa trên Google.
def open_google_and_search():
    try:
        speak("Bạn muốn tìm kiếm gì vậy?")
        time.sleep(3)
        search = str(get_text()).lower()
        url = f"https://www.google.com/search?q={search}"
        webbrowser.get().open(url)
        speak("Đây là thông tin bạn cần tìm.")
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
 #open_google_and_search()  


# Gửi email.
def send_email():
    speak("Hãy nhập tên đăng nhập email của bạn!")
    time.sleep(2)
    name = input("Tôi: Mời bạn nhập tên email đăng nhập: ") #at9274229@gmail.com
    while "@" not in name:
        print("Bot: Tên email không hợp, mời nhập lại.")
        name = input("Tôi: Mời bạn nhập tên email đăng nhập: ")
    speak("Hãy nhập mật khẩu email của bạn!")
    time.sleep(2)
    pasword = input("Tôi: Mời bạn nhập mật khẩu email: ")   #haha 123456

    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(name, pasword)
        speak("Hãy nhập tên email mà bạn muốn gửi!")     
        time.sleep(2)
        name_send = input("Tôi: Mời bạn nhập tên email muốn gửi: ")
        while "@" not in name_send:
            print("Bot: Tên email không hợp, mời nhập lại.")
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
        Bạn vui lòng kiểm tra lại lỗi bằng thông báo bên dưới!"""
            speak(error)
            time.sleep(22)
            print("Bot: {ex}".format(ex = e))
#send_email()


# Dự báo thời tiết.
def current_weather():
    try:
        speak("Bạn muốn xem thời tiết ở đâu ạ?")
        time.sleep(3)
        ow_url = "http://api.openweathermap.org/data/2.5/weather?"
        city = get_text()
        if not city:
            pass
        api_key = "fe8d8c65cf345889139d8e545f57819a"
        call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        response = requests.get(call_url)
        data = response.json()
        if data["cod"] != "404":
            city_res = data["main"]
            current_temperature = city_res["temp"]
            current_pressure = city_res["pressure"]
            current_humidity = city_res["humidity"]
            suntime = data["sys"]
            sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
            sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
            wthr = data["weather"]
            weather_description = wthr[0]["description"]
            now = datetime.datetime.now()
            content = """
            Thời tiết ở {city} như sau:
            Hôm nay là ngày {day} tháng {month} năm {year}
            Mặt trời mọc vào {hourrise} giờ {minrise} phút
            Mặt trời lặn vào {hourset} giờ {minset} phút
            Nhiệt độ trung bình là {temp} độ C
            Áp suất không khí là {pressure} héc tơ Pascal
            Độ ẩm là {humidity}%
            Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(city = city,day = now.day,month = now.month, year = now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                            hourset = sunset.hour, minset = sunset.minute, 
                                                                            temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
            speak(content)
            time.sleep(33)
        else:
            speak("Không tìm thấy địa chỉ bạn yêu cầu.")
            time.sleep(2)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#current_weather()


# Tìm kiếm và phát nhạc trên Youtube.
def play_song_in_Youtube():
    try:
        speak("Xin mời bạn chọn tên bài hát!")
        time.sleep(2)
        mysong = get_text()
        while True:
            result = YoutubeSearch(mysong, max_results = 10).to_dict()
            if result:
                break
            else:
                speak("Bài hát bạn muốn tìm không có trên youtube hoặc tiêu đề không chính xác. Xin mời bạn kiểm tra lại!")
                time.sleep(8)
                return
        url = "https://www.youtube.com" + result[0]["url_suffix"]
        webbrowser.open(url)
        speak("Bài hát bạn yêu cầu đã được mở.")
        time.sleep(3)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#play_song_in_Youtube()


# Đọc báo.
def read_news():
    try:
        speak("Bạn muốn đọc báo về chủ đề gì?")
        time.sleep(3)
        queue = get_text()
        params = {
            "apiKey": "30d02d187f7140faacf9ccd27a1441ad",
            "q": queue,
        }
        api_result = requests.get("http://newsapi.org/v2/top-headlines?", params)
        api_response = api_result.json()
        speak("Đây là tin tức về {}".format(queue))
        time.sleep(3)
        for number, result in enumerate(api_response["articles"], start = 1):
            print(f"""Tin {number}:\nTiêu đề: {result["title"]}\nTrích dẫn: {result["description"]}\nLink: {result["url"]}
        """)
            if number <= 3:
                webbrowser.open(result["url"])
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#read_news()


# Thay đổi hình nền máy tính ảnh lấy từ trên mạng.
def change_wallpaper_in_internet():
    try:
        api_key = "RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw"
        url = "https://api.unsplash.com/photos/random?client_id=" +  api_key  
        f = urllib2.urlopen(url)
        json_string = f.read()
        f.close()
        parsed_json = json.loads(json_string)
        photo = parsed_json["urls"]["full"]
        # Đường dẫn của mấy tấm ảnh nền mà mình muốn thay đổi 
        urllib2.urlretrieve(photo, f"D:\\Test\\Image\\background_test.jpg")
        image = os.path.join(f"D:\\Test\\Image\\background_test.jpg")
        ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
        speak("Hình nền máy tính vừa được thay đổi.")
        time.sleep(3)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#change_wallpaper_in_internet()


# Thay đổi hình nền được chọn từ máy tính.
def change_wallpaper_in_computer():
    try:
        speak("Bạn muốn chọn hình nào trong số những hình này để thay đổi hình nền?")
        os.startfile("D:\\Test\\Image")
        time.sleep(5)
        image = get_text()
        if os.path.exists("D:\\Test\\Image\\{image}.jpg".format(image = image)):
            path = "D:\\Test\\Image\\{image}.jpg".format(image = image)
            ctypes.windll.user32.SystemParametersInfoW(20,0,path,3)
            speak("Hình nền máy tính vừa được thay đổi.")
            time.sleep(3)
        elif os.path.exists("D:\\Test\\Image\\{image}.png".format(image = image)):
            path = "D:\\Test\\Image\\{image}.png".format(image = image)
            ctypes.windll.user32.SystemParametersInfoW(20,0,path,3)
            speak("Hình nền máy tính vừa được thay đổi.")
            time.sleep(3)
        else:
            speak("Có lẽ bạn đã phát âm sai tên của hình ảnh hoặc định dạng file không phù hợp. Vui lòng thử lại sau!")
            time.sleep(7.5)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#change_wallpaper_in_computer()


# Kể chuyện.
def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ?")
        time.sleep(2)
        text = get_text()
        contents = wikipedia.summary(text).split("\n")
        speak(contents[0].split(".")[0])
        time.sleep(10)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không?")
            time.sleep(2)
            answer = get_text()
            if "có" not in answer:
                break
            speak(content)
            time.sleep(10)

        speak("Cảm ơn bạn đã lắng nghe!")
        time.sleep(3)
    except:
        speak("Tôi không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại!")
        time.sleep(6)
#tell_me_about()


# Tìm kiếm hình ảnh trên Google.
def open_google_and_search_image(text):
    try:
        search_for = text.split("về", 1)[1]
        speak("Vâng thưa sếp!")
        driver = webdriver.Chrome(path)
        driver.get("https://images.google.com")
        que = driver.find_element_by_xpath("//input[@name='q']")
        que.send_keys(str(search_for))
        que.send_keys(Keys.RETURN)
        speak("Đây là những hình ảnh bạn cần tìm.")
        time.sleep(10)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)

    
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
#play_song_in_computer()  


# Nghe một bài át ngẫu nhiên.
def play_song_random():
    try:
        basedir = "D:\\Test\\Music\\"
        file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])
        webbrowser.open(os.path.join(basedir, file))
        speak("Một bài hát bất kì vừa được mở.")
        time.sleep(3)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#play_song_random()


# Nghe nhạc theo tâm trạng.
def play_song_according_to_mood():
    try:
        speak("Bây giờ tâm trạng của bạn như thế nào?")
        time.sleep(3)
        mood = get_text()
        if "vui" in mood:
            basedir = "D:\\Test\\Music\\Happy\\"
            file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])
            webbrowser.open(os.path.join(basedir, file))
            speak("Một bài hát vui nhộn vừa được mở.")
            time.sleep(3)
        elif "buồn" in mood:
            basedir = "D:\\Test\\Music\\Sad\\"
            file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])
            webbrowser.open(os.path.join(basedir, file))
            speak("Một bài hát buồn vừa được mở.")
            time.sleep(3)
        elif "chán" in mood:
            basedir = "D:\\Test\\Music\\Bored\\"
            file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])
            webbrowser.open(os.path.join(basedir, file))
            speak("Một bài hát giúp bạn thư giản vừa được mở.")
            time.sleep(3)
        else:
            speak("Tôi không hiểu tâm trạng này của bạn hoặc cảm xúc này chưa có bài hát nào để phát.")
            time.sleep(6)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#play_song_according_to_mood()


# Tìm file trên máy tính.
def search_file():
    try:
        speak("Xin hãy nhập ổ đĩa bạn muốn tìm file!")
        time.sleep(3)
        disk = str(input("Tôi: Mời nhập tên ổ đĩa: ")).upper()
        while disk != "C" and disk != "D":
            print("Bot: Nhập sai, mời nhập lại. Lưu ý hiện giờ tôi chỉ có thể tìm kiếm trên hai ổ đĩa C và D mà thôi.")
            disk = str(input("Tôi: Mời nhập tên ổ đĩa: ")).upper()
        speak("Xin hãy nhập tên file bạn muốn tìm kiếm. Lưu ý hãy nhập cả đuôi file.")
        time.sleep(5)
        name = input("Tôi: Nhập tên file muốn tìm: ") 
        count = 0
        list_file = []
        print("Bot: Đang tiến hành tìm kiếm...")
        for root, dirs, files in os.walk(f"{disk}:\\".format(disk = disk)):
            if name in files:
                f = os.path.join(root, name)
                list_file.append(f)
                count = count + 1
        if count == 1:        
            speak("Tìm thấy thành công file " + name + ". Dưới đây là đường dẫn của file.")
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
                file_extension  = name.rsplit(".")[-1]
                os.rename(f, path + new_name + "." + file_extension)
                speak("Đã đổi tên file.")
                print("Bot: Đường dẫn mới của file sau khi đổi tên ", path + new_name + "." + file_extension)
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
            speak("Tìm thấy thành công {count} file tên {name}. Dưới đây là đường dẫn của các file đó.".format(count = count, name = name))
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
#search_file()

# Chơi game.
def play_game():
    try:
        speak("Bạn muốn chơi game nào nhỉ?")
        time.sleep(2)
        game = get_text()
        if os.path.exists(f"D:\\Test\\Game\\{game}.exe"):
            os.startfile(f"D:\\Test\\Game\\{game}.exe") 
            speak("Game {} đã được mở.".format(game))
            time.sleep(2)
        else:
            speak("Game bạn yêu cầu chưa có trong máy hoặc sai đường dẫn. Bạn hãy kiểm tra lại nhé!")
            time.sleep(6)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#play_game()


# Cập nhật tình hình dịch Covid 19.
def update_covid_19():
    try:
        r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
        data = r.json()
        now = datetime.datetime.now()
        speak("Cập nhật tình hình dịch Covid 19 tính đến {hour} giờ {minute} phút ngày {day} tháng {month} năm {year}".format(
            hour = now.hour, minute = now.minute, day = now.day, month = now.month, year = now.year))
        time.sleep(9)
        content = """
        Tổng số ca mắc bệnh là {cases}.
        Tổng số người tử vong là {deaths}.
        Tổng số người đã khỏi bệnh là {recovered}.""".format(cases = data["cases"], deaths = data["deaths"], recovered = data["recovered"])
        speak(content)
        time.sleep(21)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#update_covid_19()


# Chụp ảnh màn hình máy tính.
def take_a_screenshot():
    try:
        path = "D:\\Test\\Image\\screenshot.png"
        pyautogui.screenshot(path)
        im = Image.open(path)
        im.save(path)
        im.show(path)
        speak("Đã chụp ảnh. Dưới đây là đường dẫn của ảnh bạn vừa chụp.")
        print("Bot: D:\\Test\\Image\\screenshot.png")
        time.sleep(5)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#take_a_screenshot()


# Dịch thuật ngôn ngữ (Ở đây chỉ gồm 3 thứ tiếng là Việt, Anh, Nhật).
def translate():
    try:
        speak("Bạn muốn dịch từ ngôn ngữ nào sang ngôn ngữ nào?")
        time.sleep(4)
        text = get_text()
        language1 = text.split()[2]
        language2 = text.split("sang tiếng ", 1)[1]

        if (str(language1) == "việt" or str(language1) == "anh" or str(language1) == "nhật") and (str(language2) == "việt" or str(language2) == "anh" or str(language2) == "nhật"):
            if str(language1) == str(language2):
                speak("Tôi không được lập trình cho tình huống kì quặc này đâu. Bạn thật hài hước!")
                time.sleep(6)
                return
            elif str(language1) == "nhật":
                speak("Xin lỗi nhưng hiện giờ tôi chưa thể nói được tiếng Nhật nên chỉ có thể dịch từ ngôn ngữ khác sang mà thôi.")
                time.sleep(8)
                return
            elif str(language1) == "việt":
                if str(language2) == "anh":
                    speak("Từ hoặc câu tiếng Việt bạn muốn dịch là gì?")
                    time.sleep(4)
                    word = get_text()
                    translate = Translator()
                    result = translate.translate("{word}".format(word = word))
                    speak('{word} trong tiếng Anh có nghĩa là "{out_word}"'.format(word = word, out_word = result.text))
                    time.sleep(5)
                else:
                    speak("Từ hoặc câu tiếng Việt bạn muốn dịch là gì?")
                    time.sleep(4)
                    word = get_text()
                    translate = Translator()
                    result = translate.translate("{word}".format(word = word), src = "vi", dest = "ja")
                    speak('Xin lỗi khi tôi không nói được tiếng Nhật nhưng {word} trong tiếng Nhật được viết như thế này: "{out_word}"'.format(word = word, out_word = result.text))
                    time.sleep(6)
            else:
                if str(language2) == "việt":
                    speak("Từ hoặc câu tiếng Anh bạn muốn dịch là gì?")
                    time.sleep(4)
                    word = get_text()
                    translate = Translator()
                    result = translate.translate("{word}".format(word = word), src = "en", dest = "vi")
                    speak('{word} trong tiếng Việt có nghĩa là "{out_word}"'.format(word = word, out_word = result.text))
                    time.sleep(5)
                else:
                    speak("Từ hoặc câu tiếng Anh bạn muốn dịch là gì?")
                    time.sleep(4)
                    word = get_text()
                    translate = Translator()
                    result = translate.translate("{word}".format(word = word), src = "en", dest = "ja")
                    speak('Xin lỗi khi tôi không nói được tiếng Nhật nhưng {word} trong tiếng Nhật được viết như thế này: "{out_word}"'.format(word = word, out_word = result.text))
                    time.sleep(6)
        else:
            speak("Tên ngôn ngữ không chính xác hoặc tôi chưa được cài gói ngôn ngữ đó.")
            time.sleep(5)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#translate()


# Tải video trên youtube về máy tính.
def download_video_youtube():
    try:
        speak("Video bạn muốn tải tên là gì nhỉ?")
        time.sleep(3)
        video = get_text()
        while True:
            result = YoutubeSearch(video, max_results = 10).to_dict()
            if result:
                break
            else:
                speak("Video bạn muốn tải không có trên youtube hoặc tiêu đề không chính xác. Xin mời bạn kiểm tra lại!")
                time.sleep(8)
                return
        url = "https://www.youtube.com" + result[0]["url_suffix"]
        file = YouTube(url).streams.filter(progressive = True, file_extension = "mp4").last().download(output_path = "D:\\Test\\Video\\")

        if os.path.exists(f"{file}"):
            speak("Đã tải video {name}".format( name = video))
            time.sleep(3)
            speak("Bạn có muốn mở video lên không?")
            time.sleep(3)
            text = get_text()
            if "có" in text:
                speak("Đã mở video.")
                time.sleep(2)
                os.startfile(f"{file}")
            else:
                return
        else:
            speak("Tải video không thành công. Bạn hãy kiểm tra lại nhé.")
            time.sleep(5)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4) 
#download_video_youtube()


# Tạo tệp tin excel.
def create_excel(input_detail, output_excel_path):
    # Xác định số hàng và cột lớn nhất trong file excel cần tạo
    row = len(input_detail)
    column = len(input_detail[0])

    # Tạo một workbook mới và active nó
    wb = openpyxl.Workbook()
    ws = wb.active
  
    # Dùng vòng lặp for để ghi nội dung từ input_detail vào file Excel
    for i in range(0,row):
        for j in range(0,column):
            v = input_detail[i][j]
            ws.cell(column = j + 1, row = i + 1, value = v)

    # Lưu lại file Excel
    wb.save(output_excel_path)   
#create_excel()


# Tạo các loại file cho máy tính. Ở đây set cứng đường dẫn luôn.
def create_file():
    try:
        speak("Bạn muốn tạo loại file gì?")
        time.sleep(2.5)
        file_type = get_text()
        if "txt" in file_type or "note pad" in file_type or "ghi chú" in file_type:
            speak("Bạn muốn đặt tên file là gì?")
            time.sleep(3)
            name = get_text()
            file = open("D:\\Test\\Test File\\{file}.txt".format(file = name), "w",encoding = "utf-8") 
            speak("Bạn muốn ghi vào file nội dung gì?")
            time.sleep(3)
            content = get_text()
            file.write(content)
            file.close()
            speak("Đã tạo file. Dưới đây là đường dẫn tới file bạn vừa tạo.")
            time.sleep(5)
            print("Bot: D:\\Test\\Test File\\{file}.txt".format(file = name))
            os.startfile("D:\\Test\\Test File\\{file}.txt".format(file = name))
        elif "word" in file_type or "văn bản" in file_type:
            speak("Bạn muốn đặt tên file là gì?")
            time.sleep(3)
            name = get_text()
            document = Document()
            speak("Bạn muốn ghi vào file nội dung gì?")
            time.sleep(3)
            content = get_text()
            document.add_paragraph(content)
            document.save("D:\\Test\\Test File\\{file}.docx".format(file = name))
            speak("Đã tạo file. Dưới đây là đường dẫn tới file bạn vừa tạo.")
            time.sleep(5)
            print("Bot: D:\\Test\\Test File\\{file}.docx".format(file = name))
            os.startfile("D:\\Test\\Test File\\{file}.docx".format(file = name))
        elif "excel" in file_type or "trang tính" in file_type:
            speak("Bạn muốn đặt tên file là gì?")
            time.sleep(3)
            name = get_text()

            input_detail =[[]]
            output_excel_path= ("D:\\Test\\Test File\\{file}.xlsx").format(file = name)
            create_excel(input_detail, output_excel_path)
            speak("Đã tạo file. Dưới đây là đường dẫn tới file bạn vừa tạo.")
            time.sleep(5)
            print("Bot: D:\\Test\\Test File\\{file}.xlsx".format(file = name))
            os.startfile("D:\\Test\\Test File\\{file}.xlsx".format(file = name))
        elif "powerpoint" in file_type or "trình chiếu" in file_type:
            speak("Bạn muốn đặt tên file là gì?")
            time.sleep(3)
            name = get_text()
            file = open("D:\\Test\\Test File\\{file}.pptx".format(file = name), "w") 
            file.close()
            speak("Đã tạo file. Dưới đây là đường dẫn tới file bạn vừa tạo.")
            time.sleep(5)
            print("Bot: D:\\Test\\Test File\\{file}.pptx".format(file = name))
            os.startfile("D:\\Test\\Test File\\{file}.pptx".format(file = name))
        else:
            speak("Tạm thời tôi chưa thể tạo được loại file này hoặc tên loại file không chính xác. Xin hãy kiểm tra lại!")
            time.sleep(8)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#create_file()


# Tạo thư mục cho máy tính. Ở đây set cứng đường dẫn luôn.
def create_folder():
    try:
        speak("Bạn muốn tạo thư mục tên gì?")
        time.sleep(2)
        text = get_text()
        dirname = "D:\\Test\\Test Folder\\" + text
        if os.path.isdir("D:\\Test\\Test Folder\\" + text) == True:
            speak("Tên thư mục đã được sử dụng cho một thư mục khác. Vui lòng chọn tên khác!")
            time.sleep(6)
            return
        else:
            os.mkdir(dirname)
    except OSError:
        speak("Tạo thư mục không thành công. Vui lòng kiểm tra lại")
        time.sleep(4)
    else:
        speak("Tạo thư mục thành công. Dưới đây là tên đường dẫn tới thư mục bạn vừa tạo.")
        time.sleep(6)
        print("Bot: " + dirname)
#create_folder()


# Tìm thư mục trên máy tính.
def search_folder():
    try:
        speak("Xin hãy nhập ổ đĩa bạn muốn tìm thư mục")
        time.sleep(3)
        disk = str(input("Tôi: Mời nhập tên ổ đĩa: ")).upper()
        while disk != "C" and disk != "D":
            print("Bot: Nhập sai, mời nhập lại. Lưu ý hiện giờ tôi chỉ có thể tìm kiếm trên hai ổ đĩa C và D mà thôi.")
            disk = str(input("Tôi: Mời nhập tên ổ đĩa: ")).upper()
        speak("Xin hãy nhập tên thư mục bạn muốn tìm kiếm.")
        time.sleep(4)
        name = input("Tôi: Nhập tên thư mục muốn tìm: ") 
        count = 0
        list_folder = []
        print("Bot: Đang tiến hành tìm kiếm...")
        for root, dirs, files in os.walk(f"{disk}:\\".format(disk = disk)):
            if name in dirs:
                f = os.path.join(root, name)
                list_folder.append(f)
                count = count + 1
        if count == 1:        
            speak("Tìm thấy thành công thư mục " + name + ". Dưới đây là đường dẫn của thư mục.")
            time.sleep(7.5)
            print("Bot: " + f)
            speak("Bạn có muốn thực hiện thao tác nào khác với thư mục vừa tìm được không?")   
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
                print("Bot: Đường dẫn mới của thư mục sau khi đổi tên ", path + new_name)
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
            speak("Tìm thấy thành công {count} thư mục tên {name}. Dưới đây là đường dẫn của các thư mục đó.".format(count = count, name = name))
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
#search_folder()


# Cài báo thức.
def set_alarm():
    try:
        note = """
        Lưu ý là khi cài báo thức thì tôi sẽ không thể thực hiện bất kì hành động nào khác cho đến khi báo thức được reo. 
        Bạn cũng không nên tắt tôi đi nếu không báo thức sẽ không reo.
        Bạn có chắc chắn muốn cài báo thức không?
        """
        speak(note)
        time.sleep(17)  
        answer = get_text()
        if "có" in answer or "ok" in answer:
            speak("Mời bạn nhập giờ và phút cho báo thức?")
            time.sleep(3)
            alarmH = input("Tôi: Mời nhập giờ: ")
            while alarmH.isdigit() == False or 0 > int(alarmH) or int(alarmH) > 23:
                print("Bot: Nhập sai, mời nhập lại")
                alarmH = input("Tôi: Mời nhập giờ: ")
            alarmM = input("Tôi: Mời nhập phút: ")
            while alarmM.isdigit() == False or 0 > int(alarmM) or int(alarmM) > 59:
                print("Bot: Nhập sai, mời nhập lại")
                alarmM = input("Tôi: Mời nhập phút: ")
            speak("Báo thức sẽ là ban ngày (am) hay từ chiều đến đêm (pm)")
            time.sleep(4)
            am_or_pm = (input("Tôi: Mời chọn am hay pm: "))
            while str(am_or_pm) != "am" and str(am_or_pm) != "pm":
                print("Bot: Nhập sai, mời nhập lại")
                am_or_pm = input("Tôi: Mời chọn am hay pm: ")
            if  "pm" == am_or_pm:
                alarmH = int(alarmH) + 12
                print("Bot: Đang chờ báo thức: {hour} giờ {minute} phút pm... ".format(hour = alarmH, minute = alarmM))
            elif "am" == am_or_pm:
                print("Bot: Đang chờ báo thức: {hour} giờ {minute} phút am... ".format(hour = alarmH, minute = alarmM))
                pass
            else:
                speak("Bạn đã không chọn đúng giá trị am hay pm. Vui lòng thử lại!")
                time.sleep(7)
                return
            while(1 == 1):
                if alarmH == datetime.datetime.now().hour and int(alarmM) == datetime.datetime.now().minute:
                    speak("Đã tới giờ báo thức!")
                    time.sleep(2)
                    playsound.playsound("D:\\Test\\Sound\\alarm.mp3")
                    time.sleep(17)
                    return
        elif "không" in answer:
            return
        else:
            speak("Tôi không hiểu câu trả lời của bạn hoặc có thể bạn đã phát âm không rõ. Vui lòng thử lại!")
            time.sleep(7)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#set_alarm()


# Tạo mã qr code.
def create_qrcode():
    try:
        speak("Xin nhập đường dẫn cho mã qr của bạn!")
        time.sleep(3)
        input_data = input("Tôi: Mời nhập đường dẫn: ")
        path_split = input_data.split(".")[0]
        while "https://www" != path_split:
            print("Bot: Dường như đường dẫn của bạn không đúng. Xin mời nhập lại!")
            input_data = input("Tôi: Mời nhập đường dẫn: ")
            path_split = input_data.split(".")[0]
        qr = pyqrcode.create(input_data)
        qr.svg("D:\\Test\\Image\\qr_code.svg", scale = 8)
        qr.png("D:\\Test\\Image\\qr_code.png", scale = 8)
        speak("Đã tạo qr code. Phía dưới là đường dẫn tới ảnh qr vừa tạo.")
        print("Bot: D:\\Test\\Image\\qr_code.png")
        time.sleep(5)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#create_qrcode()


# Tắt máy tính.
def shutdown():
    try: 
        speak("Bạn có muốn tắt máy tính của mình không?")   
        time.sleep(3)
        text = get_text()    
        if "không" in text:                
            return
        elif "có" in text:
            speak("Máy sẽ tắt sau 10 giây nữa.")   
            os.system("shutdown /s /t 10")   
            time.sleep(3) 
        else:
            speak("Tôi không hiểu câu trả lời của bạn. Vui lòng thử lại!")
            time.sleep(5)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)
#shutdown()


# Lời giới thiệu của Tố Như.
def introduce():
    intro = """
    Xin chào bạn. Rất hân hạnh được phục vụ bạn. 
    Tôi tên là Tố Như. 
    Tôi là trợ lí ảo được tạo ra dựa trên ngôn ngữ lập trình Python kết hợp với AI. 
    Tôi được tạo ra bởi các sinh viên Ngô Tấn Đăng, Hồ Sĩ Quỳnh Đức, Nguyễn Phước Hậu. 
    Hiện tại bạn đang sử dụng phiên bản 1.0 và cũng đang là phiên bản mới nhất.
    """
    speak(intro)
    time.sleep(22)
#introduce()


# Những gì mà Tố Như có thể làm và hiển thị danh sách ra.
def help_me():
    speak("Dưới đây là danh sách những việc mà tôi có thể thực hiện giúp bạn:")
    time.sleep(4.5)
    print("""
    1.  Chào hỏi.
    2.  Cho biết ngày, giờ.
    3.  Mở website, ứng dụng.
    4.  Tìm kiếm từ khóa, ảnh trên trên Google.
    5.  Gửi email.
    6.  Dự báo thời tiết.
    7.  Mở video nhạc trên Youtube.
    8.  Thay đổi hình nền máy tính bằng 2 cách:
        + Lấy ảnh từ trên mạng.
        + Lấy ảnh có sẵn trên máy tính.
    9.  Đọc báo.
    10. Kể bạn biết về thế giới bằng thông tin từ Wikipedia.
    11. Nghe nhạc có sẵn trên máy tính bằng các chế độ sau:
        + Phát một bài hát ngẫu nhiên.
        + Phát một bài hát cụ thể.
        + Phát bài hát theo tâm trạng người dùng.
    12. Tạo thư mục, các loại file.
    13. Tìm kiếm các thư mục, tập tin sau đó có thể:
        + Mở thư mục, tập tin đó lên.
        + Đổi tên thư mục, tập tin đó.
        + Xóa thư mục, tập tin đó.
    14. Tích hợp một số mini game.
    15. Cập nhật tình hình dịch bệnh Covid 19 trên thế giới.
    16. Chụp ảnh màn hình máy tính.
    17. Dịch thuật các ngôn ngữ.
    18. Tải video trên Youtube về máy tính.
    19. Cài báo thức.
    20. Tạo qr code.
    21. Tắt máy tính.
    22. Giới thiệu về bản thân của AI.
    """)            
#help_me()
    
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
                    speak("Bạn muốn lấy hình trên mạng hay hình trên máy tính?")
                    time.sleep(4)
                    text1 = get_text
                    if "trên mạng" in text1:               
                        change_wallpaper_in_internet()
                    elif "trên máy tính" in text1:
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
                    speak("Bạn muốn nghe một bài hát ngẫu nhiên hay chỉ định một bài hát cụ thể?")
                    time.sleep(5)
                    text1 = get_text()
                    if "ngẫu nhiên" in text1:               
                        play_song_random()
                    elif "cụ thể" in text1:
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
                elif "chụp ảnh màn hình" in text:
                    take_a_screenshot()
                elif "dịch thuật" in text:
                    translate()
                elif "tải video youtube" in text:
                    download_video_youtube()
                elif "tạo file" in text:
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
assistant()