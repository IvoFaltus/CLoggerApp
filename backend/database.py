import json
import secrets
import psycopg2
from psycopg2 import pool
import time

from datetime import datetime, timezone, timedelta

from werkzeug.security import generate_password_hash

import hashlib


def hash_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def hash_password(password):
    return generate_password_hash(password)


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


pool = psycopg2.pool.SimpleConnectionPool(
    1, 10,
    host=DB["host"],
    port=DB["port"],
    database=DB["database"],
    user=DB["user"],
    password=DB["password"]
)


def get_db():
    return pool.getconn()


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
        parameters = ["%s" for _ in range(len(values))]
        data = tuple(values[key] for key in values.keys())
        parameters = ",".join(parameters)

        cursor.execute(f"INSERT INTO {table}({keys}) VALUES({parameters})", data)
        conn.commit()
    finally:
        cursor.close()
        pool.putconn(conn)


def select(table, columns, condition=None):

    if table not in tables or table not in attrs:
        return None

    if not columns:
        return None

    if columns != "*":
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
        if columns == "*":
            cols = "*"
        else:
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
        pool.putconn(conn)


def query(query):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(query)
    result= cursor.fetchall()
    cursor.close()
    pool.putconn(conn)
    return result




def login(user_id):
    token = secrets.token_urlsafe(32)
    starts = datetime.now(timezone.utc)
    expires = datetime.now(timezone.utc) + timedelta(hours=24)
    token_hash = hash_token(token)

    insert("session", {
        "user_id": user_id,
        "session_token": token,
        "created_at": starts,
        "expires_at": expires
    })


if __name__ == "__main__":
    # insert("users",{"name":"jozef","lastname":"adsad","passwd_hash":"jasdfasfdozef","username":"jozef123"})
    # print(select("users",["id","name","lastname"],{"id":"4"}))
    # login(1)
    insert("users",{"name":"alex"})
    print(select("users", "*"))