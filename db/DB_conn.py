import pymysql
from core.config import settings


def get_stu_conn(): #디비연결
    return pymysql.connect(
        host = settings.DB_HOST,
        user = settings.DB_USER,
        password = settings.DB_PASSWD,
        db = settings.DB_NAME,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
