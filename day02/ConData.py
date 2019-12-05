import pymysql

def getConn():
     return pymysql.connect(host='localhost', user='root', password='123456', database='mxmm', charset='utf8')
