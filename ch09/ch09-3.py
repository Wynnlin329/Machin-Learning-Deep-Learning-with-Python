import twstock
stock = twstock.Stock('2317')  # 以鴻海的股票代號建立 Stock 物件

stock.fetch(2019,1) # 取得 2019 年 1 月的資料
stock.fetch_31()    # 取得最近 31 日的資料
stock.fetch_from(2018,10) # 取得 2018 年 11 月至今的資料