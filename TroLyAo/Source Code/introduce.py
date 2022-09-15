# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
from text_to_speech import speak


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
    time.sleep(24)


# introduce()