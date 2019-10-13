import sqlite3
con = sqlite3.connect("C:\\Users\\v\\sample.db")
print('create table')
con.execute('''CREATE TABLE testleaf('NAME','USERNAME','EMAIL','PH')''')
#Insert record
con.execute('''INSERT INTO testleaf('NAME','USERNAME','EMAIL','PH') VALUES ('vignesh','vignesh2011','vignesh2011@live.com','9600060160')''')
con.commit()
#read the data
data = con.execute('SELECT * FROM testleaf')
for i in data:
    print(i)
