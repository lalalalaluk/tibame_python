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
        sql = "DELETE FROM demo_user WHERE id = %s"
        cur.execute(sql, ("9",))
        conn.commit()
        print("刪除完成")
    except Exception as e:
        print("刪除失敗", str(e))

    cur.close()
    conn.close()
except Exception as e:
    print("連線失敗", str(e))
