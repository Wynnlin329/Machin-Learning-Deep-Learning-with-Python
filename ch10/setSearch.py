def find_face(key, secret, outer_id, pic_name):  #在人臉集合中尋找指定人臉
	url = 'https://api-cn.faceplusplus.com/facepp/v3/search' 
	data = {"api_key": key, "api_secret": secret, "outer_id": outer_id}
	files = {'image_file': open(pic_name, 'rb')}  
	r = requests.post(url,files=files,data=data)  
	return r.json()

def login(filepath):
    print('登入圖片檔案：' + filepath)
    ret = find_face(key, secret, 1, filepath)
    confidence = ret['results'][0]['confidence']  #取得最高相似度指數
    if confidence > 75:
        print('登入會員 face_token 為 ' + ret['results'][0]['face_token'])
    else:
        print('很抱歉，非會員無法登入！')

import requests

key ="你的 API Key"
secret ="你的 API Secret"

login('media/David2.jpg')    
login('media/Lily1.jpg')    
