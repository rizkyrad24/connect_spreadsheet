from fastapi import APIRouter, status
# from pydantic import BaseModel
# from typing import Union
from app.view.search import ConnectSpreadsheet

router = APIRouter()

CS = ConnectSpreadsheet()


# Ruoter Base on Existing
@router.get("/api/search", status_code=status.HTTP_200_OK)
async def log_activitas_index(sheet: str, company: str):
    return CS.search(sheet, company)

