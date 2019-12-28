def find_face(key, secret, outer_id, pic_name):  #在人臉集合中尋找指定人臉
	url = 'https://api-cn.faceplusplus.com/facepp/v3/search' 
	data = {"api_key": key, "api_secret": secret, "outer_id": outer_id}
	files = {'image_file': open(pic_name, 'rb')}  
	r = requests.post(url,files=files,data=data)  
	return r.json()

import cv2
import sqlite3
import requests
import time
from datetime import datetime

key ="你的 API Key"
secret ="你的 API Secret"

conn = sqlite3.connect('member_cloud.sqlite')  #連接資料庫
cursor = conn.cursor()
timenow = time.time()  #取得現在時間數值
cv2.namedWindow("frame")
cap = cv2.VideoCapture(0)  #開啟cam
while(cap.isOpened()):  #cam開啟成功
    count = 5 - int(time.time() - timenow)  #倒數計時5秒
    ret, img = cap.read()
    if ret == True:
        imgcopy = img.copy()  #複製影像
        cv2.putText(imgcopy, str(count), (200,400), cv2.FONT_HERSHEY_SIMPLEX, 15, (0,0,255), 35)  #在複製影像上畫倒數秒數
        cv2.imshow("frame", imgcopy)  #顯示複製影像
        k = cv2.waitKey(100)  #0.1秒讀鍵盤一次
        if k == ord("z") or k == ord("Z") or count == 0:  #按「Z」鍵或倒數計時結束
            cv2.imwrite("media/tem.jpg", img)  #將影像存檔
            break
cap.release()  #關閉cam
cv2.destroyWindow("frame")
ret = find_face(key, secret, 1, "media/tem.jpg")
confidence = ret['results'][0]['confidence']
if confidence > 75:
    token = ret['results'][0]['face_token']
    sqlstr = 'SELECT * FROM member WHERE facetoken="' + token +'"'
    cursor.execute(sqlstr)
    row = cursor.fetchone()
    print('登入成功！歡迎 ' + row[0] + '！' )
    savetime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  #目前時刻字串
    sqlstr = 'INSERT INTO login values("{}","{}")'.format(row[0], savetime)  #將帳號及現在時刻寫入資料表
    cursor.execute(sqlstr)
    conn.commit()
else:
    print('很抱歉，非會員無法登入！')

conn.close()

