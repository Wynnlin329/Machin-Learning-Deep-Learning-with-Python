import speech_recognition as sr

r = sr.Recognizer()  #建立語音辨識物件
with sr.WavFile("record1.wav") as source:  #讀取語音檔
    audio = r.record(source)

print('開始翻譯...')
try:
    text = r.recognize_google(audio, language="zh-TW")  #辨識結果
    print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition 無法辨識此語音！")
except sr.RequestError as e:
    print("無法由 Google Speech Recognition 取得結果; {0}".format(e))
print('翻譯結束！')
    