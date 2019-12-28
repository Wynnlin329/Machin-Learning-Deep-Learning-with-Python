import sqlite3

conn = sqlite3.connect('member_cloud.sqlite')  #連接資料庫
cursor = conn.cursor()
sqlstr = 'SELECT * FROM login'  #讀取登入資料表
cursor.execute(sqlstr)
rows = cursor.fetchall()  #取得登入資料
print('%-15s %-20s' % ('帳號','登入時間'))
print('=============== ====================')
for row in rows:  
    print('%-15s %-20s' % (row[0], row[1]))

conn.close()
