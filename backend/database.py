import json
import mysql.connector

with open("config.json") as f:
    DB = json.load(f)

def get_db():
    return mysql.connector.connect(
        host=DB["host"],
        port=DB["port"],
        database=DB["database"],
        user=DB["user"],
        password=DB["password"]
    )


if __name__ == "__main__":
    conn = get_db()
    print("Database connection successful:", conn.is_connected())

    cursor = conn.cursor()
    cursor.execute("select * from users;")
    tables = cursor.fetchall()
    print("Tables in the database:", tables)
    cursor.close()

    conn.close()

   
    # CREATE TABLE users (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     username VARCHAR(40) NOT NULL,
    #     password VARCHAR(255) NOT NULL
        
    # );
    # CREATE TABLE country(
    # id INT AUTO_INCREMENT PRIMARY KEY,
    # name varchar(30) not null

    # );

    # CREATE TABLE clients (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     name VARCHAR(20) NOT NULL,
    #     surname VARCHAR(30) NOT NULL,
    #     phone varchar(30) not null,
    #     email VARCHAR(50) CHECK (email LIKE '%@%.%') not null,
    #     created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    #     active BOOLEAN DEFAULT TRUE,
    #     updated_at DATETIME 
    #         DEFAULT CURRENT_TIMESTAMP 
    #         ON UPDATE CURRENT_TIMESTAMP,
    #     vip BOOLEAN default false,
    #     country_id INT,
    # FOREIGN KEY (country_id) REFERENCES country(id)

    # );

    #     CREATE TABLE user_client (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     user_id INT NOT NULL,
    #     client_id INT NOT NULL,
    #     role VARCHAR(30),
    #     assigned_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    #     FOREIGN KEY (user_id) REFERENCES users(id),
    #     FOREIGN KEY (client_id) REFERENCES clients(id),
    #     UNIQUE (user_id, client_id)
    # );
    # CREATE TABLE payment (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     user_client_id INT NOT NULL,
    #     amount FLOAT NOT NULL,
    #     paid BOOLEAN DEFAULT FALSE,
    #     paid_at DATETIME,

    #     FOREIGN KEY (user_client_id) REFERENCES user_client(id)
    # );
    # CREATE TABLE note (
    #     id INT AUTO_INCREMENT PRIMARY KEY,
    #     user_id INT NOT NULL,
    #     client_id INT NOT NULL,
    #     text VARCHAR(255) NOT NULL,
    #     created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    #     FOREIGN KEY (user_id) REFERENCES users(id),
    #     FOREIGN KEY (client_id) REFERENCES clients(id)
    # );







