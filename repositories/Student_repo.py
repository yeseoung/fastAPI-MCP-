from db.DB_conn import get_stu_conn
from pymysql.cursors import DictCursor

def get_students():
    conn = get_stu_conn()
    try:
        with conn.cursor(DictCursor) as cursor:
            sql = "SELECT * FROM stu;"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()

def get_student_by_id(student_id : int):
    conn = get_stu_conn()
    try:
        with conn.cursor(DictCursor) as cursor:
            sql = "SELECT * FROM stu where student_id = %s;"
            cursor.execute(sql,(student_id,))
            return cursor.fetchone()
    finally:
        conn.close()

def get_student_by_name(student_name : str):  
    conn = get_stu_conn()
    try:
        with conn.cursor(DictCursor) as cursor:
            sql = "SELECT * FROM stu where name = %s;"
            cursor.execute(sql,(student_name,))
            return cursor.fetchone()
    finally:
        conn.close()

def get_random_students(limit=5):
    conn = get_stu_conn()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT name, student_id FROM stu ORDER BY RAND() LIMIT %s"
            cursor.execute(sql, (limit,))
            result = cursor.fetchall()
            return result
    finally:
        conn.close()
