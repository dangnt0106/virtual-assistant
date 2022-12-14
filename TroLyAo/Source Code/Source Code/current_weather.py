# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import requests
import datetime
from text_to_speech import speak
from get_text import get_text

# Dự báo thời tiết.
def current_weather():
    try:
        speak("Bạn muốn xem thời tiết ở đâu ạ?")
        time.sleep(3)
        ow_url = "http://api.openweathermap.org/data/2.5/weather?"
        city = get_text().title()
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
            Hôm nay là ngày {day} tháng {month} năm {year}.
            Mặt trời mọc vào {hourrise} giờ {minrise} phút.
            Mặt trời lặn vào {hourset} giờ {minset} phút.
            Nhiệt độ trung bình là {temp} độ C.
            Áp suất không khí là {pressure} héc tơ Pascal.
            Độ ẩm là {humidity}%.
            Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(city=city, day=now.day, month=now.month, year=now.year, hourrise=sunrise.hour, minrise=sunrise.minute,
                                                                               hourset=sunset.hour, minset=sunset.minute,
                                                                               temp=current_temperature, pressure=current_pressure, humidity=current_humidity)
            speak(content)
            time.sleep(33)
        else:
            speak("Không tìm thấy địa chỉ bạn yêu cầu.")
            time.sleep(3)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# current_weather()