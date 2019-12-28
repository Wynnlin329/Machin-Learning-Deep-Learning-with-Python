import sqlite3

conn = sqlite3.connect('member_local.sqlite')
cursor = conn.cursor()
sqlstr = 'CREATE TABLE IF NOT EXISTS member("memberid" TEXT, "picture" TEXT)'  #會員資料表
cursor.execute(sqlstr)
sqlstr = 'CREATE TABLE IF NOT EXISTS login("memberid" TEXT, "ltime" TEXT)'  #登入資料表
cursor.execute(sqlstr)
conn.commit()

conn.close()