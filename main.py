from fastapi import FastAPI
import asyncio

from fastapi.staticfiles import StaticFiles
from api.student_api import router as student_router
from api.whoami import router as IPdetecter
from api.Authlogin import router as Auth_router
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(student_router)
app.include_router(Auth_router)
app.include_router(IPdetecter)

app.mount("/", StaticFiles(directory="static", html=True), name="static")
