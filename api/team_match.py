from fastapi import APIRouter, HTTPException, Body, Request, Query
import json
import random
import pymysql
from db.DB_conn import get_stu_conn

router = APIRouter()

def get_random_students(count=5):
    conn = get_stu_conn()
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT name, student_id FROM stu ORDER BY RAND() LIMIT %s"
            cursor.execute(sql, (count,))
            result = cursor.fetchall()
            return result
    finally:
        conn.close()

@router.get("/match")
async def match(request: Request):
    try:
        random_team = get_random_students(5)
        if not random_team or len(random_team) == 0:
            raise HTTPException(status_code=404, detail="stu 테이블에 학생 데이터가 없습니다.")
        return {"team": random_team}
    except Exception as e:
        print(f"매칭 에러 발생: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/confirm")
async def confirm_team(data: dict = Body(...)):
    print(f"수신된 데이터: {data}")
    conn = get_stu_conn()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO teams (team_name, members, leader) VALUES (%s, %s, %s)"
            members_json = json.dumps(data['members'], ensure_ascii=False)
            cursor.execute(sql, (data['team_name'], members_json, data['leader']))
            conn.commit()
            print("DB 저장 성공!")
            return {"status": "success", "message": "팀 저장 완료"}
    except Exception as e:
        conn.rollback()
        print(f"DB 저장 에러 상세: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@router.get("/my-teams")
async def get_my_teams(username: str = Query(...)): # Query 파라미터 명시 ✅
    conn = get_stu_conn()
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            # leader 컬럼까지 포함해서 가져오기
            sql = "SELECT team_name, members, leader, created_at FROM teams WHERE leader = %s ORDER BY created_at DESC"
            cursor.execute(sql, (username,))
            result = cursor.fetchall()
            
            for row in result:
                # 1. members JSON 문자열을 리스트로 변환 ✅
                if isinstance(row['members'], str):
                    row['members'] = json.loads(row['members'])
                
                # 2. 날짜 객체를 문자열로 변환 (JSON 에러 방지 핵심!) ✅
                if row['created_at']:
                    row['created_at'] = row['created_at'].strftime("%Y-%m-%d %H:%M:%S")
                    
            return {"teams": result}
    except Exception as e:
        print(f"목록 조회 중 에러 발생: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()