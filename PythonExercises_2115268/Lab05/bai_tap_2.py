import pyodbc

connectionString ='''DRIVER={ODBC Driver 17 for SQL Server};SERVER=ThanhLa; DATABASE=QLySinhVien;UID=thanhla;PWD=123456;Encrypt=no'''

def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()
        

def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query = "select * from Lop"
        cursor.execute(select_query)
        
        
        records = cursor.fetchall()
        
        print(f"Danh sách các lớp là: ")
        for row in records:
            print("*"*50)
            print("Mã số", row[0])
            print("Họ và yên", row[1]
            print("Mã lớp",))
            
        
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)
        
def gte_all_student():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query = "select * from SinhVien"
        cursor.execute(select_query)
        
        
        records = cursor.fetchall()
        
        print(f"Danh sách tất cả sinh viên là: ")
        for row in records:
            print("*"*50)
            print("Mã lớp", row[0])
            print("Tên lớp", row[1])
            
        
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)
    

def get_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query =" select * from Lop where id = ?"
        
        params =(class_id,)
        cursor.execute(select_query, params)
        
        record = cursor.fetchone()
        
        print(f"Thông tin có lớp có id = {class_id} là:")
        print("Mã lớp:", record[0])
        print("Tên lớp:", record[1])
        
        close_connection(connection)
    except(Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)



#def insert_class(class_name):
    #try:
        #connection = get_connection()
        #cursor = connection.cursor()
        
        
        #Cách 1 - truyền trực tiếp tham số vào câu truy vấn
        #select_query =""
        #Cách 2
        #select_query = "Insert into Lop(TenLop) values ( ? )"
        #cursor.execute(select_query, (class_name,))
        
        #connection.commit()
        
        #print("Đã thêm thành công")
        
        #close_connection(connection)
    #except(Exception, pyodbc.Error) as error:
        #print(" Đã có lỗi xảy ra khi thực thi. Thông tin lỗi:", error)
        
#insert_class("CTK44AB")
get_all_class()    
get_class_by_id(2)

    