import json
import secrets
import psycopg2
from psycopg2 import pool
import time
import re


from datetime import datetime, timezone, timedelta

from werkzeug.security import generate_password_hash,check_password_hash

import hashlib



def generate_session_token():
    token = secrets.token_urlsafe(32)
    print(token)
    return token


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

def delete(table, condition=None):

    if table not in tables or table not in attrs:
        return None

    if condition is not None:
        for key in condition.keys():
            if key not in attrs[table]:
                return None

    conn = get_db()
    cursor = conn.cursor()

    try:
        if condition is None or len(condition) == 0:
            query = f"DELETE FROM {table};"
            cursor.execute(query)
        else:
            where_string = " AND ".join(f"{key}=%s" for key in condition.keys())
            parameters = tuple(condition[key] for key in condition.keys())
            query = f"DELETE FROM {table} WHERE {where_string};"

            print(query, parameters)  
            cursor.execute(query, parameters)

        print("deleted rows:", cursor.rowcount)

        conn.commit()

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



def login_user(username):

    user_id = select("users", ["id"], {"username": username})[0][0]

    token = secrets.token_urlsafe(32)
    starts = datetime.now(timezone.utc)
    expires = starts + timedelta(hours=24)
    token_hash = hash_token(token)

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO user_session (user_id, session_token, created_at, expires_at)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (user_id)
            DO UPDATE SET
                session_token = EXCLUDED.session_token,
                created_at = EXCLUDED.created_at,
                expires_at = EXCLUDED.expires_at;
        """, (user_id, token_hash, starts, expires))

        conn.commit()

    finally:
        cursor.close()
        pool.putconn(conn)

    return token

def create_user(username, name, lastname, password):
    if not (name and lastname and username and password):
        return {"msg": "error"}

    name_pattern = r"^[A-Z][a-z]{1,49}$"
    lastname_pattern = r"^[A-Z][a-z]{1,49}$"
    username_pattern = r"^[a-zA-Z0-9_]{4,20}$"
    password_pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,50}$"

    # validation
    if not re.match(name_pattern, name):
        return {"msg": "name_error"}

    if not re.match(lastname_pattern, lastname):
        return {"msg": "lastname_error"}

    if not re.match(username_pattern, username):
        return {"msg": "username_format_error"}

    if not re.match(password_pattern, password):
        return {"msg": "password_error"}

    exists = select("users", ["username"], {"username": username})
    if exists:
        return {"msg": "username_exists_error"}

    passwd_hash = hash_password(password)

    insert("users", {
        "name": name,
        "lastname": lastname,
        "username": username,
        "passwd_hash": passwd_hash
    })

    return {"msg": "success"}
    
def deleteSession(sessionid):
    if not sessionid: return None
    hashed = hash_token(sessionid)
    delete("user_session",{"session_token":hashed})





def authenticate(username,passwd):
    passwdhash = select("users", ["passwd_hash"],{"username":username})
    if not passwdhash:
        return None
    passwdhash=passwdhash[0][0]
    return check_password_hash(passwdhash,passwd)
def verify(sessionid):
    if not sessionid:
        return False
    id_from_db = select("user_session",["session_token"],{"session_token":hash_token(sessionid)})
    
    if(id_from_db):
        return True
    
    
    return False
    

def getUser(request):
    token = request.cookies.get("sessionid")
    userid = select("user_session",["user_id"],{"session_token":token})
    username = select("user",["username"],{"id":userid})
    
    


if __name__ == "__main__":
   
    #insert("users",{"name":"jozef","lastname":"lastname","passwd_hash":hash_password("heslo"),"username":"test67"})
   
     delete("users",{"username":"test67"})