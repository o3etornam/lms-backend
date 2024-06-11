from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..database import get_db
from .. import models
from .. import schema
from .. import utils
from .. import oauth2


router = APIRouter(
    tags=['Authentication']
)

@router.post('/login', response_model=schema.FrontendData)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends()
                ,db:AsyncSession = Depends(get_db)):
    # OAuth2PasswordRequestFor stores what the user enters in a dictionary 
    # w key words username and password
    select_query = select(models.User).where(models.User.email == user_credentials.username)
    result = await db.execute(select_query)
    user = result.scalar_one_or_none()
    
    if user:
        if await utils.verify(user_credentials.password, user.password):
            access_token = await oauth2.create_access_token(data = {'user_id':user.id})
            token_data = {'access_token': access_token, 'token_type':'bearer'}
            user_public = schema.UserPublic(email=user.email, firstName=user.firstName,
                                            lastName=user.lastName, role=user.role)
            return schema.FrontendData(token=token_data,user=user_public)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='invalid credentials')
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail=f'user with email {user_credentials.username} not found')