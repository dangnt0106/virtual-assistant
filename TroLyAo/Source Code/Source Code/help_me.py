# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
from text_to_speech import speak


# Những gì mà Tố Như có thể làm và hiển thị danh sách ra.
def help_me():
    speak("Dưới đây là danh sách những việc mà tôi có thể thực hiện giúp bạn:")
    time.sleep(4.5)
    print("""
    1.  Tự động kiểm tra kết nối mạng Internet (Lưu ý là không có mạng Internet thì AI không hoạt động).
    2.  Chào hỏi.                                              
    3.  Cho biết ngày, giờ. 
    4.  Mở website, ứng dụng.
    5.  Tìm kiếm từ khóa, hình ảnh trên Google.
    6.  Gửi email.
    7.  Dự báo thời tiết.
    8.  Mở video nhạc trên Youtube.
    9.  Thay đổi hình nền máy tính bằng 2 cách:
        + Lấy ảnh từ trên mạng.
        + Lấy ảnh có sẵn trên máy tính.
    10.  Đọc báo.
    11. Kể bạn biết về thế giới bằng thông tin từ Wikipedia.
    12. Nghe nhạc có sẵn trên máy tính bằng các chế độ sau:
        + Phát một bài hát ngẫu nhiên.
        + Phát một bài hát cụ thể.
        + Phát bài hát theo tâm trạng người dùng.
    13. Tạo thư mục, các loại file.
    14. Tìm kiếm các thư mục, tập tin sau đó có thể:
        + Mở thư mục, tập tin đó lên.
        + Đổi tên thư mục, tập tin đó.
        + Xóa thư mục, tập tin đó.
    15. Tích hợp một số mini game.
    16. Cập nhật tình hình dịch bệnh Covid 19 trên thế giới.
    17. Cập nhật tình hình giá vàng trên thị trường.
    18. Chụp ảnh màn hình máy tính.
    19. Dịch thuật các ngôn ngữ.
    20. Tải video trên Youtube về máy tính.
    21. Cài báo thức.
    22. Tạo mã qr code.
    23. Tắt máy tính.
    24. Giới thiệu về bản thân của AI.
    """)


# help_me()