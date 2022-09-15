# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
import requests
import webbrowser
from text_to_speech import speak
from get_text import get_text


# Đọc báo.
def read_news():
    try:
        speak("Bạn muốn đọc báo về chủ đề gì?")
        time.sleep(3)
        queue = get_text().title()
        params = {
            "apiKey": "30d02d187f7140faacf9ccd27a1441ad",
            "q": queue,
        }
        print("Bot: Đang tiến hành tìm kiếm các bài báo...")
        api_result = requests.get(
            "http://newsapi.org/v2/top-headlines?", params)
        api_response = api_result.json()
        speak('Dưới đây là danh sách tin tức về "{}". Lưu ý là nếu không tìm được kết quả thì sẽ không có danh sách.'.format(queue))
        time.sleep(8)
        for number, result in enumerate(api_response["articles"], start=1):
            print(f"""\tTin {number}\n\tTiêu đề: {result["title"]}\n\tTrích dẫn: {result["description"]}\n\tLink: {result["url"]}
            """)
            if number <= 3:
                webbrowser.open(result["url"])
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# read_news()