import sqlite3 as lite
conn = lite.connect("test.db")
print("Done")
conn.execute('''CREATE TABLE if not exists COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print("Table created successfully")
conn.execute("""INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) 
      VALUES (1, 'Paul', 32, 'California', 20000.00 )""")

conn.execute("""INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) 
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )""")

conn.execute("""INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) 
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )""")

conn.execute("""INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) 
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )""")
print("dones")
cursor=conn.execute(""" select * from company""")
for x in cursor:
    print(x)