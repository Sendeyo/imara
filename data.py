import sqlite3


def data_write(query):
    conn = sqlite3.connect("Members.db")
    conn.execute(query)
    conn.commit()
    conn.close()


def read(query):
    data = []
    conn = sqlite3.connect("Members.db")
    cursor = conn.execute(query)
    for row in cursor:
        data.append(row)
    conn.close()
    return data


def readRaw():
    conn = sqlite3.connect("Members.db")
    cursor = conn.execute(query)
    

