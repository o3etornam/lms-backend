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

@router.post('', status_code=201, response_model=schema.UserPublic)
async def create_user(user: schema.UserCreate, db:AsyncSession = Depends(get_db)):
    # user.role = user.role.value
    user.password = await utils.hash(user.password)
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@router.get('', response_model= list[schema.UserPublic])  
async def get_users(db:AsyncSession = Depends(get_db)):
    select_query = select(models.User)
    users = await db.execute(select_query)
    return users.scalars().all()

@router.get('/{id}', response_model= schema.UserPublic)
async def get_user(id: str, db:AsyncSession = Depends(get_db)):
    select_query = select(models.User).where(models.User.id == id)
    result = await db.execute(select_query)
    user = result.scalar_one_or_none()
    
    if user:
        return user
    raise HTTPException(status_code=404, detail=f'User with id {id} doesn\'t exsit')
