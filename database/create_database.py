import psycopg2

try:
    conn = psycopg2.connect(
        host="dpg-clr7qsae9h4c73at0oe0-a.oregon-postgres.render.com",
        dbname="mypostgresql_sak8",
        user="postgresql",
        password="CjgIg6UnHbUnlW3RgdnWW6LaCRnwpZkZ",
    )
    print("連線成功")

    cur = conn.cursor()

    try:
        sql = "INSERT INTO demo_user (account, passwd) VALUES (%s,%s)"
        cur.execute(sql, ("mary", "qwer"))
        conn.commit()
        print("新增完成")
    except Exception as e:
        print("新增失敗", str(e))

    cur.close()
    conn.close()
except Exception as e:
    print("連線失敗", str(e))
