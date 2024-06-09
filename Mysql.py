import mysql.connector as connection_obj
database=input('Enter Database Name')
connector = connection_obj.connect(host='localhost', user='root', password='npol', database=f"{database}")
cursor = connector.cursor()


def create():
    global dummy
    columns = []
    dummy = ''
    tablename = input('Enter table Name')
    column_no = int(input('Enter columns no'))
    for i in range(column_no):
        column_name = input('Enter Column Name ex Price,Name.. etc')
        data_type = input('Enter Data Type of the columns eg int,varchar(x)')
        columns.append([column_name, data_type])
        """ columns is [[column1,datatype],[column2,datatype]]"""
    for ColumnName, DataType in columns:
        dummy = f"{dummy} {ColumnName} {DataType}, "
    query = f"CREATE TABLE {tablename} ({dummy[0:len(dummy) - 2]});"
    print(query)
    cursor.execute(query)
    connector.commit()
    cursor.close()
    connector.close()
    print('DONE')


def read():
    Table_Name = input('Enter table Name')
    query = f"select * from {Table_Name};"
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)


def insert():
    rows = int(input('Enter Number of rows'))
    Table_Name = input('Enter table Name')
    for count in range(rows):
        PROD_ID = input('Enter Prod ID')
        PROD_NAME = input('Enter Product Name')
        PRICE = int(input('Enter Price'))
        COMPANY = input('Enter Company')
        TYPE = input('Enter Type')
        Query = f"insert into {Table_Name} values('{PROD_ID}','{PROD_NAME}',{PRICE},'{COMPANY}','{TYPE}');"
        print(Query)
        cursor.execute(Query)
        connector.commit()
    cursor.close()
    connector.close()


while True:
    print("""
    1.Create
    2.Read
    3.Insert
    4.Break""")
    choice = int(input('Enter Choice:'))
    if choice == 1:
        create()
    elif choice == 2:
        read()
    elif choice == 3:
        insert()
    else:
        break
