from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Pydantic model for login request
class LoginRequest(BaseModel):
    email: str
    password: str

# Simulated user database (replace with real database logic)
fake_users_db = {
    "test@example.com": {"password": "123456"}
}

@router.post("/login")
async def login(request: LoginRequest):
    user = fake_users_db.get(request.email)
    if not user or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    return {"message": "Login successful"}
