from cmath import log
from fastapi import APIRouter
from src.endpoints import login, node
router = APIRouter()
router.include_router(login.router)
router.include_router(node.router)