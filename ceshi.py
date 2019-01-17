import pymysql

def ljsql(sq):
    db = pymysql.connect("192.168.199.72", "root", "123qwe", "amp")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sq)

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print(data)

    # 关闭数据库连接
    db.close()
# wxsum=ljsql("select * FROM amp.current_threat_info where severity =3 group by assets_id")
