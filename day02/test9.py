import pymysql

from day02 import ConData

if __name__ == '__main__':
    conn = ConData.getConn()
    cursor = conn.cursor()
    sql = "INSERT INTO USER1(name, age) VALUES (%s, %s);"
    data = [('aaa',18),('bbb',19),('ccc',20)]

    try:
        cursor.executemany(sql,data);
        conn.commit()
    except Exception as e:
        conn.rollback()

    cursor.close()
    conn.close()