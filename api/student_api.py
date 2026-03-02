from fastapi import APIRouter, HTTPException, Depends
from DTO.student import student_Response
from repositories.Student_repo import *
from typing import List
from fastapi.responses import JSONResponse
from AUTH.deps import get_current_user  #(그냥 토큰 검증임 ㅇㅇ)

router = APIRouter(
    prefix="/students",
    tags=["students"],
    dependencies=[Depends(get_current_user)]  # 전체 라우터 보호
)

@router.get("/", response_model=List[student_Response])
async def get_student_list():
    students = get_students()
    if not students:
        raise HTTPException(status_code=404, detail="Student not found")
    return JSONResponse(
        content=students,
        media_type="application/json; charset=utf-8"
    )

@router.get("/id/{student_id}", response_model=student_Response)
async def get_by_id(student_id: int):
    student = get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return JSONResponse(
        content=student,
        media_type="application/json; charset=utf-8"
    )

@router.get("/name/{student_name}", response_model=student_Response)
async def get_by_name(student_name: str):
    student = get_student_by_name(student_name)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return JSONResponse(
        content=student,
        media_type="application/json; charset=utf-8"
    )
