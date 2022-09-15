# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import requests
import json
import time
from text_to_speech import speak


# Cập nhật giá vàng trên thị trường.
def update_gold_price():
    try:
        url = "https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now"
        resp = requests.get(url)
        resp.encoding = "utf-8-sig"
        content = resp.text.encode().decode("utf-8-sig")
        return json.loads(content)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


'''
a = update_gold_price()
b = a["golds"]
c = b[0]
d = c["value"]
speak("Dưới đây là bảng danh sách mới nhất của giá vàng trên thị trường.")
time.sleep(5)
for i in d:
    print("\t|-----------------------------------------------------------------------------------------------------------------------------------------|")
    print("\t Giá mua:  {0}   Giá bán:  {1}   Loại vàng:  {2}   Cập nhật lúc {3} tại {4}.".format(
        i["buy"], i["sell"], i["type"], i["updated"], i["brand"]))
    print("\t|-----------------------------------------------------------------------------------------------------------------------------------------|")
'''