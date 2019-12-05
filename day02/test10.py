from day02 import  ConData

class User:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

if __name__ == '__main__':
    conn = ConData.getConn()
    cursor = conn.cursor()
    sql = "SELECT id,name,age from USER1 WHERE id=1;"
    cursor.execute(sql)
    # ret = User(cursor.fetchone())
    ret = cursor.fetchone()
    print(ret)
    print(ret)
    cursor.close()
    conn.close()


