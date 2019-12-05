import pymysql
if __name__ == '__main__':
    conn = pymysql.connect(host='localhost',user='root', password='123456', database= 'mxmm', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = """
    CREATE TABLE USER1 (
    id INT auto_increment PRIMARY KEY ,
    name CHAR(10) NOT NULL UNIQUE,
    age TINYINT NOT NULL
    )ENGINE=innodb DEFAULT CHARSET=utf8;
    """
    aa = cursor.execute(sql)
    print(aa)
    cursor.close()
    conn.close()