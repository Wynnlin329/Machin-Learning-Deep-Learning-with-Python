import requests
from json import JSONDecoder

def compareimage(filepath1 ,filepath2):  #人臉比對
    try:
        http_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
        key = "你的 API Key"
        secret = "你的 API Secret"
        data = {"api_key":key, "api_secret": secret}
        files = {"image_file1": open(filepath1, "rb"),"image_file2": open(filepath2, "rb")}
        response = requests.post(http_url, data=data, files=files)  #進行辨識
        req_con = response.content.decode('utf-8')  #取得結果
        req_dict = JSONDecoder().decode(req_con)  #將結果轉為字典
        confidence = req_dict['confidence']  #取得相似度指數
        return confidence
    except Exception:
        print("產生錯誤，無法識別！")
        return 0

def showcompare(filepath1 ,filepath2):
    result = compareimage(filepath1 ,filepath2)
    print('相似度指數=' + str(result))
    if result >= 75:
        print(filepath1+' 和 '+filepath2+' 為同一人！')
    else:
        print(filepath1+' 和 '+filepath2+' 為不同人！')

showcompare('media/David1.jpg', 'media/face1.jpg')
showcompare('media/jeng1.jpg', 'media/face1.jpg')
