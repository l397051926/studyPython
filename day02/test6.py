import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', user='root', password='123456', database='mxmm', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO USER1(name, age) VALUES (%s, %s);"
    userName = 'xiaoMing'
    age = 12
    cursor.execute(sql, [userName, age])
    print("插入成功！~！！")
    conn.commit()
    cursor.close()
    conn.close()
