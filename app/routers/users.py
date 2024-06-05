from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from .. import models
from .. import schema
from .. import utils



router = APIRouter(
    prefix= "/users",
    tags= ['Users']
)



@router.post('', status_code=201, response_model=schema.UserPublic)
async def create_user(user: schema.UserCreate, db:AsyncSession = Depends(get_db)):
    # user.role = user.role.value
    user.password = await utils.hash(user.password)
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
    