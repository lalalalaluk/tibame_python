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

    sql = "SELECT * FROM demo_user"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
except Exception as e:
    print("連線失敗", str(e))
