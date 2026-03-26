import psycopg

def get_db():
    return psycopg.connect(
        host="193.85.203.186",
        dbname="test",
        user="postgres",
        port=5432
    )

def select_users():
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()
        return rows
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    result = select_users()
    for row in result:
        print(row)











        durationMap = {

            "monthly":1,
            "daily":2,
            "weekly":3,
        }