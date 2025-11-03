from fastapi import APIRouter, Depends

from src.banking.services import create_account_number



router = APIRouter(prefix="/banking", tags=["banking"])

