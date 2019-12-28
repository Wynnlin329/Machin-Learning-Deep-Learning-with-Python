def upload(key, secret, filepath):  #上傳圖片
    url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    files = {'image_file':open(filepath, "rb")}
    data = {'api_key': key, 'api_secret': secret}
    response = requests.post(url, data=data, files=files)
    data = json.loads(response.text)
    face_tokens = data['faces'][0]['face_token']  #取得圖片token
    print(filepath + ': ' + face_tokens)
    return face_tokens  #傳回圖片token
    
def add(key, secret, faceset_token, face_tokens):  #在人臉集合加入圖片
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"
    data = {"api_key": key, "api_secret": secret, "faceset_token": faceset_token, "face_tokens": face_tokens}
    response = requests.post(http_url, data=data)
    req_dic = json.loads(response.text)
    print("Add face:",req_dic)
    return req_dic

import json
import requests

key ="你的 API Key"
secret ="你的 API Secret"
faceset_token = '77f6b2b55de164aa0d33be482b57be5f'

face_tokens = upload(key, secret, 'memberPic/David.jpg')
add(key, secret, faceset_token, face_tokens)
face_tokens = upload(key, secret, 'memberPic/Bear.jpg')
add(key, secret, faceset_token, face_tokens)
