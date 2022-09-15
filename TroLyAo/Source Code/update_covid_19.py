# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import requests
import datetime
import time
from text_to_speech import speak


# Cập nhật tình hình dịch Covid 19.
def update_covid_19():
    try:
        r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
        data = r.json()
        now = datetime.datetime.now()
        speak("Cập nhật tình hình dịch Covid 19 tính đến {hour} giờ {minute} phút ngày {day} tháng {month} năm {year}.".format(
            hour=now.hour, minute=now.minute, day=now.day, month=now.month, year=now.year))
        time.sleep(9)
        content = """
        Tổng số ca mắc bệnh là {cases}.
        Tổng số người tử vong là {deaths}.
        Tổng số người đã khỏi bệnh là {recovered}.""".format(cases=data["cases"], deaths=data["deaths"], recovered=data["recovered"])
        speak(content)
        time.sleep(21)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# update_covid_19()