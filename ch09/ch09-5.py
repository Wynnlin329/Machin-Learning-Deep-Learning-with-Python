import csv
import pandas as pd
import twstock
import os

filepath = 'twstockmonth01.csv'

if not os.path.isfile(filepath):  #如果檔案不存在就建立檔案   
    stock = twstock.Stock('2317')  # 以鴻海的股票代號建立 Stock 物件
    stocklist=stock.fetch(2018,1)  # 2018 年 1 月
    
    title=["日期","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"]
    data=[]
    for stock in stocklist:
        strdate=stock.date.strftime("%Y-%m-%d") #  將datetime物件轉換為字串
        # 讀取 日期,成交股數,成交金額,開盤價,最高價,最低價,收盤價,漲跌價差,成交筆數
        li=[strdate,stock.capacity,stock.turnover,stock.open,stock.high,\
            stock.low,stock.close,stock.change,stock.transaction]
        data.append(li) 
    
    outputfile = open(filepath,'w',newline='',encoding='big5')  #開啟檔案
    outputwriter = csv.writer(outputfile)  #以csv格式寫入檔案
    outputwriter.writerow(title) #寫入標題
    for dataline in (data):      #寫入資料
        outputwriter.writerow(dataline)
    outputfile.close()  #關閉檔案

pdstock = pd.read_csv(filepath, encoding='big5')  #以pandas讀取檔案
pdstock['日期'] = pd.to_datetime(pdstock['日期'])  #轉換日期欄位為日期格式
pdstock.plot(kind='line', figsize=(12, 6), x='日期', y=['收盤價', '最低價', '最高價'])  #繪製統計圖 