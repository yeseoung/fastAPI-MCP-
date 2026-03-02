from db.DB_conn import get_stu_conn
from pymysql.cursors import DictCursor

#역할: 데이터베이스와 직접 통신
#특징: SQL 실행, 결과 반환, DB 연결 관리
#주의: API 계층(FastAPI 라우터)에서는 반환값을 받아서 직접 응답 처리만 하면 됨

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