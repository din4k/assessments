"""
This module will perform CURD of records on database table 
"""

import pymysql.cursors


def read_records():
    conn = get_connection()
    sql = """SELECT * FROM test.users"""
    run_query(conn, sql)
    return

def add_record(name, age, email):
    conn = get_connection()
    print("Added...entry with values {}, {}, {}".format(name, age, email))
    sql = """INSERT INTO test.users(name, age, email) VALUES ('{}', '{}', '{}')""".format(name, int(age), email)
    run_query(conn, sql)
    return

def del_record(rec_id):
    conn = get_connection()
    sql = """DELETE FROM test.users WHERE id = {}""".format(int(rec_id))
    run_query(conn, sql)
    return

def modify_record(rec_id, **kwargs):
    conn = get_connection()
    print("Modified... entry with values {}".format(rec_id))
    sql =  """UPDATE test.users SET email = 'dinesh4k@hotmail.com' WHERE id = 2"""
    run_query(conn, sql)
    return

def get_connection():
    SERVER_URL = "localhost"
    DB = "test"
    USER_NAME = "root"
    PASSWORD = "1Blue8eagle!234"

    SQL_CONNECTION = pymysql.connect(host=SERVER_URL,
                    user=USER_NAME,
                    passwd=PASSWORD,
                    db=DB,
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor,
                    autocommit=True)
    return SQL_CONNECTION

def run_query(conn, sql):
    SQL_CONNECTION = conn
    SQL = sql
    
    with SQL_CONNECTION.cursor() as cursor:
        try:
            sql_exec = cursor.execute(SQL)
            if sql_exec:
                print(sql_exec)
                print(cursor.fetchall())
            else:
                print(sql_exec)
                print("No Record")
        except (pymysql.Error, pymysql.Warning) as e:
            print("error! {}".format(e))
        
        finally:
            SQL_CONNECTION.close()
    return

if __name__ == '__main__':
    read_records()
#    add_record('DG',41,'dink@yahoo.com')
#    del_record(2)
#    modify_record(1, name='Kumar')

