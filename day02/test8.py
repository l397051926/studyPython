import pymysql

from day02 import ConData

if __name__ == '__main__':
    conn = ConData.getConn()
    cursor = conn.cursor()

    sql = "INSERT INTO USER1(name, age) VALUES (%s, %s);"

    name = 'liSi'
    age = '13'

    cursor.execute(sql, [name,age])
    conn.commit()
    last_id = cursor.lastrowid
    print(last_id)
    cursor.close()
    conn.close()
