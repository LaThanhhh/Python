import pyodbc

#print(pyodbc.drivers())
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=ThanhLa; DATABASE=QLMonAn;UID=thanhla;PWD=123456')
cursor = conn.cursor()

cursor.execute("SELECT @@VERSION")

data = cursor.fetchall()
#print(data)

db_version = cursor.fetchone()
conn.close()
print("Bạn đang dùng hệ quản trị CSDL server phiên bản ", db_version)
#