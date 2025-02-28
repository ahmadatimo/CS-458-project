from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from fastapi import Response
import httpx

router = APIRouter()

# Constants
MAX_ATTEMPTS = 5
LOCKOUT_DURATION = timedelta(minutes=1)  # Lock user for 10 minutes
SPOTIFY_CLIENT_ID = "57d5a4acd20548fb89c5ceccec77332c"  # Replace with your Spotify Client ID
SPOTIFY_CLIENT_SECRET = "af2a2c607df5443f852fce77c6aae0ec"  # Replace with your Spotify Client Secret
SPOTIFY_REDIRECT_URI = "http://localhost:3000/Successful"  # Replace with your redirect URI

# Pydantic model for login request
class LoginRequest(BaseModel):
    email: str
    password: str

# Simulated user database (replace with real database logic)
users_db = {
    "test@example.com": {"password": "abc123", "failed_attempts": 0, "lockout_time": None},
    "lupin@hogwarts.com": {"password": "eatCh0klate", "failed_attempts": 0, "lockout_time": None},
    "john.doe@example.com": {"password": "password123", "failed_attempts": 0, "lockout_time": None},
    "alice.smith@example.com": {"password": "alice123", "failed_attempts": 0, "lockout_time": None},
    "bob.jones@example.com": {"password": "bobpass", "failed_attempts": 0, "lockout_time": None},
    "charlie.brown@example.com": {"password": "charlie2025", "failed_attempts": 0, "lockout_time": None},
    "eve.white@example.com": {"password": "eve1234", "failed_attempts": 0, "lockout_time": None},
    "david.green@example.com": {"password": "david2025", "failed_attempts": 0, "lockout_time": None},
}

@router.post("/login")
def login(request: LoginRequest):
    user = users_db.get(request.email)

    def reset_lockout():
        user["failed_attempts"] = 0
        user["lockout_time"] = None

    def check_lockout():
        remaining_time = (user["lockout_time"] - datetime.now()).seconds  # Get remaining seconds
        raise HTTPException(status_code=403, detail=f"Too many failed attempts. Try again in {remaining_time} seconds.")

    def lockout_mechanism():
        user["lockout_time"] = datetime.now() + LOCKOUT_DURATION
        check_lockout()

    def check_length():
        if len(request.password) <= 5:
            raise HTTPException(status_code=403, detail="password must be at least 5 characters")

        if len(request.password) >= 15:
            raise HTTPException(status_code=403, detail="password must be at most 15 characters")

        if not any(c.isalpha() for c in request.password) or not any(c.isdigit() for c in request.password):
            raise HTTPException(status_code=403, detail="password must contain numbers and letters")

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

        check_length()

        if user["failed_attempts"] >= MAX_ATTEMPTS:
            lockout_mechanism()

        raise HTTPException(status_code=401, detail="Invalid password try again")

    return {"message": "✅ Login successful!"}

@router.post("/logout")
async def logout(response: Response):
    print("User logged out")  # Debugging
    response.delete_cookie(key="auth_token")
    return {"message": "✅ Logout successful!"}

# Spotify OAuth callback endpoint
@router.get("/spotify/callback")
async def spotify_callback(request: Request, response: Response):
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code missing")

    # Exchange code for access token
    async with httpx.AsyncClient() as client:
        try:
            token_response = await client.post(
                "https://accounts.spotify.com/api/token",
                data={
                    "grant_type": "authorization_code",
                    "code": code,
                    "redirect_uri": SPOTIFY_REDIRECT_URI,
                    "client_id": SPOTIFY_CLIENT_ID,
                    "client_secret": SPOTIFY_CLIENT_SECRET,
                },
            )
            token_response.raise_for_status()
            token_data = token_response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=400, detail=f"Failed to exchange code for token: {e.response.text}")

    # Check for errors in the response
    if "error" in token_data:
        raise HTTPException(status_code=400, detail=token_data["error"])

    # Fetch user data using the access token
    access_token = token_data.get("access_token")
    if not access_token:
        raise HTTPException(status_code=400, detail="Failed to get access token")

    async with httpx.AsyncClient() as client:
        try:
            user_response = await client.get(
                "https://api.spotify.com/v1/me",
                headers={"Authorization": f"Bearer {access_token}"},
            )
            user_response.raise_for_status()
            user_data = user_response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=400, detail=f"Failed to fetch user data: {e.response.text}")

    # Create a session or token for the user
    user_token = "some_generated_token"  # Replace with a real token (e.g., JWT)
    response.set_cookie(key="auth_token", value=user_token, httponly=True, max_age=3600)  # Set a cookie

    return {
        "message": "✅ Spotify login successful!",
        "user": {
            "spotify_id": user_data.get("id"),
            "display_name": user_data.get("display_name"),
            "email": user_data.get("email"),  # Only available if you requested the `user-read-email` scope
        },
    }

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="auth_token")  # Remove auth token
    return {"message": "✅ Logout successful!"}

