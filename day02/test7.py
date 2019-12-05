import pymysql
if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', user='root', password='123456', database='mxmm', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO USER1(name, age) VALUES (%s, %s);"
    name = 'xiaoLi2'
    age = 133
    try:
        cursor.execute(sql, [name,age])
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    cursor.close()
    conn.close()
