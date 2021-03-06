def compareimage(filepath1 ,filepath2):  #人臉比對
    try:
        http_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
        key = "gy_hiRw4eQr4HXO3h3ccaPIgaeIEH0kZ"
        secret = "lf0foQiX_JaG3q6YN6pXPpW3ctfMJFwV"
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

import cv2
import sqlite3
import requests
from json import JSONDecoder
import time
from datetime import datetime

conn = sqlite3.connect('member_local.sqlite')  #連接資料庫
cursor = conn.cursor()
sqlstr = 'SELECT * FROM member'  #讀取會員資料表
cursor.execute(sqlstr)
rows = cursor.fetchall()  #取得會員資料
imagedict = {}  #會員帳號、檔名字典
for row in rows:  
    imagedict[row[0]] = 'memberPic/' + row[1]

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

success = False  #記錄登入是否成功
for img in imagedict:  #逐一比對會員圖片
    if compareimage(imagedict[img], "media/tem.jpg") > 75:  #相似度大於75
        print('登入成功！歡迎 ' + img + '！' )
        success = True
        savetime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  #目前時刻字串
        sqlstr = 'INSERT INTO login values("{}","{}")'.format(img, savetime)  #將帳號及現在時刻寫入資料表
        cursor.execute(sqlstr)
        conn.commit()
        break
if not success:  #登入失敗
    print('登入失敗！你不是會員！')

conn.close()
