#!/usr/bin/python

# Meine este Version eine SQLite DB auzulesen

import sqlite3
conn = sqlite3.connect('thw.db')

c = conn.cursor()
for row in c.execute('SELECT * FROM helferdaten'):
            print(row)

# Einzelabfrage in einer Zeile
# c.execute("SELECT * FROM helferdaten")
# print(c.fetchall())
