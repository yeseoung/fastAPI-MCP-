from fastapi import Request
from fastapi import APIRouter,HTTPException

router = APIRouter()

@router.get("/whoami")
def whoami(request: Request):
    ip = request.headers.get("x-forwarded-for")
    if ip:
        ip = ip.split(",")[0]  # 첫 번째가 실제 사용자
    else:
        ip = request.client.host

    return {"ip": ip}