import sqlite3
import datetime
import os
from urllib.parse import unquote


def insert_data_to_db(IIN, row_name, value="empty"):
    connect = sqlite3.connect("data_about_candidat_HCSBK.db")

    connect.cursor()

    connect.execute("""
        CREATE TABLE IF NOT EXISTS Candidat_Data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        IIN INTEGER NOT NULL,
        FIO TEXT NOT NULL,
        Phone TEXT NOT NULL,
        Birthday TEXT,
        SelectEducation TEXT,
        BirthPlace TEXT,
        email TEXT,
        Dolzhnost TEXT,
        date_ TEXT
        );
        """)
    print("row_name")
    connect.execute(
        f"UPDATE Candidat_Data SET {row_name}='{unquote(value)}' WHERE IIN={IIN}")

    connect.commit()
    connect.close()


def save_new_candidat(IIN, FIO="empty", Phone="empty", Birthday="empty", SelectEducation="empty", BirthPlace="empty", email="empty", Dolzhnost="empty"):
    connect = sqlite3.connect("data_about_candidat_HCSBK.db")

    connect.cursor()

    connect.execute("""
        CREATE TABLE IF NOT EXISTS Candidat_Data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        IIN INTEGER NOT NULL,
        FIO TEXT NOT NULL,
        Phone TEXT NOT NULL,
        Birthday TEXT,
        SelectEducation TEXT,
        BirthPlace TEXT,
        email TEXT,
        Dolzhnost TEXT,
        date_ TEXT
        );
        """)

    date_ = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    connect.execute(
        "INSERT INTO Candidat_Data (IIN, FIO, Phone, Birthday, SelectEducation, BirthPlace, email, Dolzhnost, date_) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);",
        (IIN, FIO, Phone, Birthday, SelectEducation, BirthPlace, email, Dolzhnost, date_))
    connect.commit()
    connect.close()


def check_exist_status_IIN(IIN, db_name, table_name, coloumn_name="IIN"):
    connect = sqlite3.connect(os.path.join(os.getcwd(), db_name))
    connect.cursor()
    connect.commit()

    rows = connect.execute(f"SELECT {coloumn_name} FROM {table_name}").fetchall()
    connect.close()
    print("rows ", rows)
    exist_status = False
    print("IIN in db", IIN)
    for row in rows:
        print(type(row[0]))
        if IIN in row:
            print("row", row)
            print(type(row))
            print("len row", len(row))
            exist_status = True
            return exist_status
    return exist_status