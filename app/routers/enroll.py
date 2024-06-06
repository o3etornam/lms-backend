from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from .. import models
from .. import schema
from .. import utils



router = APIRouter(
    prefix= "/enroll",
    tags= ['Enrollement']
)

@router.post('.add')
async def add_user():
    pass
