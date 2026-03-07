import json
import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool

with open("config.json") as f:
    DB = json.load(f)

def get_tables():
    result = None
    with open("tables.json") as f:
        result = json.load(f)
        result = result["tables"]
    return result    


def get_attrs():
    result = None
    with open("attributes.json") as f:
        result = json.load(f)
    return result   


tables = get_tables()
attrs = get_attrs()

pool = MySQLConnectionPool(
    pool_name="client_pool",
    pool_size=10,
    host=DB["host"],
    port=DB["port"],
    database=DB["database"],
    user=DB["user"],
    password=DB["password"]
)

def get_db():
    return pool.get_connection()


def insert(table, values):

    if table not in tables or table not in attrs:
        return None

    if not values:
        return None

    for key in values.keys():
        if key not in attrs[table]:
            return None

    conn = get_db()
    cursor = conn.cursor()

    try:
        keys = ",".join(values.keys())
        parameters = ["%s" for s in range(len(values))]
        data = tuple(values[key] for key in values.keys())
        parameters = ",".join(parameters)

        cursor.execute(f"INSERT INTO {table}({keys}) VALUES({parameters})", data)
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def select(table, columns, condition=None):

    if table not in tables or table not in attrs:
        return None

    if not columns:
        return None

    for key in columns:
        if key not in attrs[table]:
            return None

    if condition is not None:
        for key in condition.keys():
            if key not in attrs[table]:
                return None

    conn = get_db()
    cursor = conn.cursor()

    try:
        cols = ",".join(columns)

        if condition is None:
            cursor.execute(f"SELECT {cols} FROM {table};")
        else:
            string = " AND ".join(f"{key}=%s" for key in condition.keys())
            parameters = tuple(condition[key] for key in condition.keys())
            cursor.execute(f"SELECT {cols} FROM {table} WHERE {string};", parameters)

        result = cursor.fetchall()
        return result

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    #insert("users",{"name":"jozef","lastname":"adsad","passwd_hash":"jasdfasfdozef","username":"jozef123",})
    print(select("users",["id","name","lastname"],{"id":"4"}))