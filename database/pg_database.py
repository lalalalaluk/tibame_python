import psycopg2


class Postgres:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="dpg-clr7qsae9h4c73at0oe0-a.oregon-postgres.render.com",
                dbname="mypostgresql_sak8",
                user="postgresql",
                password="CjgIg6UnHbUnlW3RgdnWW6LaCRnwpZkZ",
            )
            print("連線成功")
        except Exception as e:
            print("連線失敗", str(e))

    def __del__(self):
        if self.conn:
            self.conn.close()
            print("連線結束")

    def read(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()

    def create(self, sql, value):
        try:
            cur = self.conn.cursor()
            cur.execute(sql, value)
            self.conn.commit()
            print("新增完成")
            cur.close()
        except Exception as e:
            print("新增失敗", str(e))

    def create_multi(self, sql, value):
        try:
            cur = self.conn.cursor()

            cur.executemany(sql, value)
            self.conn.commit()
            print("新增多筆完成")
            cur.close()
        except Exception as e:
            print("新增多筆失敗", str(e))

    def update(self, sql, value):
        try:
            cur = self.conn.cursor()
            cur.execute(sql, value)
            self.conn.commit()
            print("更新完成")
            cur.close()
        except Exception as e:
            print("更新失敗", str(e))

    def delete(self, sql, value):
        try:
            cur = self.conn.cursor()
            cur.execute(sql, value)
            self.conn.commit()
            print("刪除完成")
            cur.close()
        except Exception as e:
            print("刪除失敗", str(e))


if __name__ == "__main__":
    my_db = Postgres()

    # my_db.create(
    #     "INSERT INTO demo_user (account, passwd) VALUES (%s,%s)", ("Jack", "jj1234")
    # )

    # datas = [("apple", "aaa1234"), ("banana", "bbb1234"), ("lemon", "lll1234")]
    # my_db.create_multi("INSERT INTO demo_user (account, passwd) VALUES (%s,%s)", datas)

    # my_db.update(
    #     "UPDATE demo_user SET passwd = %s WHERE id = %s", ("new_password", "8")
    # )

    my_db.delete("DELETE FROM demo_user WHERE id = %s", ("11",))

    my_db.read("SELECT * FROM demo_user ORDER BY id")
