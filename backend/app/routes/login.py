from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Pydantic model for login request
class LoginRequest(BaseModel):
    email: str
    password: str

# Simulated user database (replace with real database logic)
fake_users_db = {
    "test@example.com": {"password": "123456"},
    "mona@gmail.com": {"password": "mona"},
    "john.doe@example.com": {"password": "password123"},
    "alice.smith@example.com": {"password": "alice123"},
    "bob.jones@example.com": {"password": "bobpass"},
    "charlie.brown@example.com": {"password": "charlie2025"},
    "eve.white@example.com": {"password": "eve1234"},
    "david.green@example.com": {"password": "david2025"}
}


@router.post("/login")
async def login(request: LoginRequest):
    user = fake_users_db.get(request.email)
    if not user or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    return {"message": "Login successful"}
