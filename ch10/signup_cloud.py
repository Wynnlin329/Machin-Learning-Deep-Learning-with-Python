def upload(key, secret, filepath):  #上傳圖片
    url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    files = {'image_file':open(filepath, "rb")}
    data = {'api_key': key, 'api_secret': secret}
    response = requests.post(url, data=data, files=files)
    data = json.loads(response.text)
    face_tokens = data['faces'][0]['face_token']  #取得圖片token
    print('face_tokens: ' + face_tokens)
    return face_tokens  #傳回圖片token
    
def add(key, secret, faceset_token, face_tokens):  #在人臉集合加入圖片
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"
    data = {"api_key": key, "api_secret": secret, "faceset_token": faceset_token, "face_tokens": face_tokens}
    response = requests.post(http_url, data=data)
    req_dic = json.loads(response.text)
    return req_dic

import cv2
import sqlite3
import json
import requests

key ="你的 API Key"
secret ="你的 API Secret"
faceset_token = '77f6b2b55de164aa0d33be482b57be5f'

conn = sqlite3.connect('member_cloud.sqlite')  #連接資料庫
cursor = conn.cursor()
sqlstr = 'SELECT * FROM member'  #讀取會員資料表
cursor.execute(sqlstr)
rows = cursor.fetchall()  #取得會員資料
member = []
for row in rows:  #儲存所有會員帳號
    member.append(row[0])
while True:
    memberid = input('輸入帳號 (直接按「Enter」結束)：')
    if memberid == '':  #未輸入帳號就結束
        break
    elif memberid in member:  #帳號已存在
        print('此帳號已存在，不可重複！')
    else:  #建立帳號
        cv2.namedWindow("frame")
        cap = cv2.VideoCapture(0)  #開啟cam
        while(cap.isOpened()):  #如果cam已開啟
            ret, img = cap.read()  #讀取影像
            if ret == True:
                cv2.imshow("frame", img)  #顯示影像
                k = cv2.waitKey(100)  #0.1秒檢查一次按鍵
                if k == ord("z") or k == ord("Z"):  #按下「Z」鍵
                    cv2.imwrite('media/tem.jpg', img)  #儲存影像
                    break
        cap.release()  #關閉cam
        cv2.destroyWindow("frame")
        face_tokens = upload(key, secret, 'media/tem.jpg')
        add(key, secret, faceset_token, face_tokens)
        sqlstr = 'INSERT INTO member values("{}","{}")'.format(memberid, face_tokens)  #將帳號及人臉特徵人臉特徵稱寫入資料表
        cursor.execute(sqlstr)
        conn.commit()
        print('帳號建立成功！')

conn.close()

