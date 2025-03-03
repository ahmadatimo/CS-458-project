# CS-458 Project

## Project Overview
This project aims to develop a web application, which consists of a **frontend** built with React and a **backend** built with FastAPI. Users will be able to register, log in (using email/password, Google authentication, and Facebook authentication).

## Tasks
- [ ] Implement user authentication (login, Google login, Facebook login, Spotify login)
- [ ] Write unit tests for backend and frontend components
- [ ] Automate testing using Selenium

## Repository Structure
```
CS-458-PROJECT/
│── backend/x
│   ├── app/
│   │   ├── __pycache__/
│   │   ├── database/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── users_db.py
│   │   ├── managers/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── AuthManager.py
│   │   │   ├── LockoutManager.py
│   │   │   ├── LoginManager.py
│   │   │   ├── LogoutManager.py
│   │   │   ├── PasswordValidator.py
│   │   │   ├── SpotifyOAuthManager.py
│   │   │   ├── UserManager.py
│   │   ├── models/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── LoginRequest.py
│   │   ├── routes/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   ├── login.py
│   │   ├── __main__.py
│   │   ├── main.py
│   ├── venv/   # Virtual environment (not included in repo)
│
│── frontend/
│   ├── node_modules/  # Dependencies (not included in repo)
│   ├── public/
│   │   ├── vite.svg
│   ├── src/
│   │   ├── assets/
│   │   │   ├── vite.svg
│   │   ├── components/
│   │   │   ├── GoogleLoginComponent.tsx
│   │   │   ├── NormalLoginComponent.tsx
│   │   │   ├── SpotifyLoginComponent.tsx
│   │   ├── pages/
│   │   │   ├── LoginPage.tsx
│   │   │   ├── SuccessfulPage.tsx
│   │   ├── App.tsx
│   │   ├── index.css
│   │   ├── main.tsx
│   │   ├── vite-env.d.ts
│   ├── .gitignore
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── postcss.config.js
│   ├── README.md
│   ├── tailwind.config.js
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   ├── vite.config.ts
│
│── selenium/  # Placeholder for Selenium tests
│   ├──project_1/
│   │   ├── chromedriver.exe   # for windows
│   │   ├── chromedriver       # for macOS/Linux
│   │   ├── run_tests.py
│   │   ├── test1.py
│   │   ├── test2.py
│   │   ├── test3.py
│   │   ├── test4.py
│   │   ├── test5.py
│
│── .cache_ggshield # git Gaurdian for protection granted by Spotify API
│── README.md  # Project documentation
```

## How to Run the Project

### Running the Backend
#### Prerequisites:
- Python 3.x installed
- FastAPI and dependencies installed

#### Steps:
1. Navigate to the backend folder:
   ```sh
   cd backend
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate      # On Windows 
   source venv/Scripts/activate #On Mac
   ```
3. Install dependencies:
   ```sh
   pip install fastapi uvicorn
   ```
4. Run the backend server:
   ```sh
   python -m app #On Windows
   python3 -m app #On Mac
   ```
   The backend should now be running at `http://localhost:8000`.
   The backend endpoints should be running at `http://localhost:8000/docs`.

### Running the Frontend
#### Prerequisites:
- npm installed

#### Steps:
1. Navigate to the frontend folder:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the frontend development server:
   ```sh
   npm run dev
   ```
   The frontend should now be accessible at `http://localhost:3000`.

### Running the test files (Selenium)
#### Prerequisites:
- google chrome installed
- having latest Chromedriver compatible with chrome version (already in selenium/project_1/)

#### Steps:
1. Install dependencies:  
   ```sh
   pip install selenium
   ```
2. Navigate to the selenium folder:
   ```sh
   cd selenium/project_1
   ```
3. Run a specific test file, for example, test1.py:
   ```sh
   python test1.py
   ```
4. Run all test files (optional):
   ```sh
   python run_tests.py
   ```
NOTE: uncomment 8th and comment 11th line of each test if you are a macOS/Linux user. Ifyou are windows user then tests are prepared for you.
---


