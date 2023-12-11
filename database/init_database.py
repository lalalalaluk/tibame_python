import psycopg2

try:
    conn = psycopg2.connect(
        host="dpg-clr7qsae9h4c73at0oe0-a.oregon-postgres.render.com",
        dbname="mypostgresql_sak8",
        user="postgresql",
        password="CjgIg6UnHbUnlW3RgdnWW6LaCRnwpZkZ",
    )
    print("連線成功")
except Exception as e:
    print("連線失敗", str(e))
