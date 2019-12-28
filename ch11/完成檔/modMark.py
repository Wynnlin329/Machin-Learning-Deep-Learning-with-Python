fp = open('Haar-Training_carPlate/training/positive/info.txt', 'r')
line = fp.readline()
rettext = ''
print('開始轉換圖框！')
while line:
    data = line.split(' ')
    n = data[1]
    rettext += data[0] + ' ' + n + ' '
    #讀取原來資料
    for i in range(int(n)):
        x = float(data[2+i*4])
        y = float(data[3+i*4])
        w = float(data[4+i*4])
        h = float(data[5+i*4])
        if (w/h) < 3.8:  #如果寬長比小於3.8
            newW = h * 3.8  #寬=高*3.8
            x -= int((newW - w) / 2)  #計算新X位置
            if x<=0:  x=0
            w = int(newW)
        rettext = rettext+str(int(x))+' '+data[3+i*4]+' '+str(int(w))+' '+data[5+i*4]
    line = fp.readline()
fp.close()

fp = open('Haar-Training_carPlate/training/positive/info.txt', 'w')
fp.write(rettext) 
fp.close()   
print('轉換圖框結束！')
