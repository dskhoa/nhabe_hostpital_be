import os
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt

from repositories.user import UserRepository

bearer_scheme = HTTPBearer()
SECRET_KEY = os.getenv('SECRET_KEY', 'nhabehospital')
ALGORITHM = os.getenv('ALGORITHM', 'HS256')
user_repository = UserRepository()
excluded_endpoints = ["/", "/docs", "/openapi.json", "/token", "/report/create/"]


async def check_bearer_token(request: Request, call_next):
    if request.url.path in excluded_endpoints:
        # Skip token validation for excluded endpoints
        response = await call_next(request)
        return response

    # Get the Authorization header from the request
    auth_header = request.headers.get("Authorization")

    # Check if the Authorization header exists and starts with "Bearer "
    if auth_header and auth_header.startswith("Bearer "):
        # Extract the token from the header
        token = auth_header.split(" ")[1]
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = decoded_token.get("sub")

        # Check if the token is valid
        if not username:
            raise HTTPException(status_code=401, detail="Invalid bearer token")

        # Token is valid, proceed with the request
        response = await call_next(request)
        return response

    # Authorization header is missing or invalid
    raise HTTPException(status_code=401, detail="Invalid bearer token")

