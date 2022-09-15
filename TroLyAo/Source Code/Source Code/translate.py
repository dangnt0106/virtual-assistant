# Import các thư viện và các file cần thiết cho quá trình tạo nên trợ lí ảo.
import time
from text_to_speech import speak
from get_text import get_text
from text_to_speech_japanese import speak_japanese
from googletrans import Translator


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
                speak(
                    "Tôi không được lập trình cho tình huống kì quặc này đâu. Bạn thật hài hước!")
                time.sleep(6)
                return
            elif str(language1) == "việt":
                if str(language2) == "anh":
                    speak("Từ hoặc câu tiếng Việt bạn muốn dịch là gì?")
                    time.sleep(4)
                    word = get_text()
                    translate = Translator()
                    result = translate.translate("{word}".format(word=word))
                    speak('"{word}" trong tiếng Anh được phát âm là "{out_word}".'.format(
                        word=word, out_word=result.text))
                    time.sleep(7.5)
                else:
                    speak("Từ hoặc câu tiếng Việt bạn muốn dịch là gì?")
                    time.sleep(4)
                    word = get_text()
                    translate = Translator()
                    result = translate.translate(
                        "{word}".format(word=word), src="vi", dest="ja")
                    speak(
                        '"{word}" trong tiếng Nhật được phát âm là: '.format(word=word))
                    time.sleep(7.5)
                    speak_japanese("{out_word}".format(out_word=result.text))
                    time.sleep(5)
            elif str(language1) == "anh":
                if str(language2) == "việt":
                    speak("Từ hoặc câu tiếng Anh bạn muốn dịch là gì?")
                    time.sleep(4)
                    word = get_text()
                    translate = Translator()
                    result = translate.translate(
                        "{word}".format(word=word), src="en", dest="vi")
                    speak('"{word}" trong tiếng Việt được phát âm là "{out_word}".'.format(
                        word=word, out_word=result.text))
                    time.sleep(7.5)
                else:
                    speak("Từ hoặc câu tiếng Anh bạn muốn dịch là gì?")
                    time.sleep(4)
                    word = get_text()
                    translate = Translator()
                    result = translate.translate(
                        "{word}".format(word=word), src="en", dest="ja")
                    speak(
                        '"{word}" trong tiếng Nhật được phát âm là: '.format(word=word))
                    time.sleep(7.5)
                    speak_japanese("{out_word}".format(out_word=result.text))
                    time.sleep(5)
            else:
                if str(language2) == "việt":
                    speak("Hãy nhập từ hoặc câu tiếng Nhật bạn muốn dịch!")
                    time.sleep(4)
                    word = input(
                        "Tôi: Mời nhập (Lưu ý là cần nhập chữ Hiragana, Katakana, Kanji thì mới dịch được): ")
                    translate = Translator()
                    result = translate.translate(
                        "{word}".format(word=word), src="ja", dest="vi")
                    speak_japanese("{word}".format(word=word))
                    time.sleep(5)
                    speak('Trong tiếng Việt được phát âm là "{out_word}".'.format(
                        out_word=result.text))
                    time.sleep(6)
                else:
                    speak("Hãy nhập từ hoặc câu tiếng Nhật bạn muốn dịch!")
                    time.sleep(4)
                    word = input(
                        "Tôi: Mời nhập (Lưu ý là cần nhập chữ Hiragana, Katakana, Kanji thì mới dịch được): ")
                    translate = Translator()
                    result = translate.translate(
                        "{word}".format(word=word), src="ja", dest="en")
                    speak_japanese("{word}".format(word=word))
                    time.sleep(5)
                    speak('Trong tiếng Anh được phát âm là "{out_word}".'.format(
                        out_word=result.text))
                    time.sleep(6)
        else:
            speak(
                "Tên ngôn ngữ không chính xác hoặc tôi chưa được cài các gói ngôn ngữ đó. Vui lòng thử lại sau!")
            time.sleep(7)
    except:
        speak("Đã xảy ra lỗi. Vui lòng thử lại sau!")
        time.sleep(4)


# translate()