from datetime import datetime , timedelta
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Constants
MAX_ATTEMPTS = 5
LOCKOUT_DURATION = timedelta(minutes=5)  # Lock user for 10 minutes


# Pydantic model for login request
class LoginRequest(BaseModel):
    email: str
    password: str

# Simulated user database (replace with real database logic)
fake_users_db = {
    
    "test@example.com": {"password": "abc123","failed_attempts": 0,"lockout_time": None}, 
    "lupin@hogwarts.com": {"password": "eatCh0klate","failed_attempts": 0,"lockout_time": None},
    "john.doe@example.com": {"password": "password123","failed_attempts": 0,"lockout_time": None},
    "alice.smith@example.com": {"password": "alice123","failed_attempts": 0,"lockout_time": None},
    "bob.jones@example.com": {"password": "bobpass","failed_attempts": 0,"lockout_time": None},
    "charlie.brown@example.com": {"password": "charlie2025","failed_attempts": 0,"lockout_time": None},
    "eve.white@example.com": {"password": "eve1234","failed_attempts": 0,"lockout_time": None},
    "david.green@example.com": {"password": "david2025","failed_attempts": 0,"lockout_time": None},
}


@router.post("/login")
def login(request: LoginRequest):
    user = fake_users_db.get(request.email)

    def reset_lockout():
        user["failed_attempts"] = 0
        user["lockout_time"] = None

    def check_lockout():
        remaining_time = (user["lockout_time"] - datetime.now()).seconds  # Get remaining seconds
        raise HTTPException(status_code=403, detail=f"Too many failed attempts. Try again in {remaining_time} seconds.")

    def lockout_mechanisim(): 
        user["lockout_time"] = datetime.now() + LOCKOUT_DURATION
        check_lockout()
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email")

    # If lockout time has expired, reset attempts
    if user["lockout_time"] and datetime.now() > user["lockout_time"]:
        reset_lockout()

    # Check if the user is locked out
    if user["lockout_time"] and datetime.now() < user["lockout_time"]:
        check_lockout()

    # Check password (this is a simple check; use hashing in real applications)
    if request.password != user["password"]:
        user["failed_attempts"] += 1

        if len(request.password) <= 5:
            raise HTTPException(status_code=403, detail="password must be at least 5 characters")
        
        if len(request.password) >= 15:
            raise HTTPException(status_code=403, detail="password must be at most 15 characters")

        if user["failed_attempts"] >= MAX_ATTEMPTS:
            lockout_mechanisim()

        raise HTTPException(status_code=401, detail="Invalid password try again")

    return {"message": "✅ Login successful!"}