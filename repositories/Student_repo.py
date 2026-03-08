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

def get_random_students(limit=5):
    conn = get_stu_conn()  # 기존에 만드신 DB 연결 함수
    try:
        with conn.cursor() as cursor:
            # SQL의 RAND() 함수를 사용해 행을 섞고 지정한 수만큼 가져옵니다.
            sql = "SELECT name, student_id FROM stu ORDER BY RAND() LIMIT %s"
            cursor.execute(sql, (limit,))
            result = cursor.fetchall()
            return result # 리스트 형태 [{name: '...', student_id: '...'}, ...]
    finally:
        conn.close()