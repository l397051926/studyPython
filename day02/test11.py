from day02 import ConData

if __name__ == '__main__':
    conn = ConData.getConn()
    cursor = conn.cursor()
    sql = "SELECT id,name,age from USER1;"
    cursor.execute(sql)
    ret = cursor.fetchall()
    cursor.close()
    conn.close()
    print(ret)
