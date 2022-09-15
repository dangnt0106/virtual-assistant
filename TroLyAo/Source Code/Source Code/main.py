# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import urllib.request as urllib2
import time


# Trước hết kiểm tra kết nối mạng Internet.
def check_Internet_Urllib(url="http://google.com", timeout=3):
    try:
        urllib2.urlopen(url, timeout=timeout)
        from assistant import assistant
        print("\nBot: Kết nối Internet đã sẵn sàng.")
        assistant()
    except Exception as e:
        print("Bot: Đã có lỗi gì đó xảy ra hoặc bạn vui lòng kiểm tra lại kết nối Internet! Tôi chỉ hoạt động khi có kết nối Internet.")
        time.sleep(10)


check_Internet_Urllib()