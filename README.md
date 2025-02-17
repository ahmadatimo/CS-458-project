# CS-458 Project

## Project Overview
This project aims to develop a web application, which consists of a **frontend** built with React and a **backend** built with FastAPI. Users will be able to register, log in (using email/password, Google authentication, and Facebook authentication).

## Tasks
- [ ] Implement user authentication (login, Google login, Facebook login)
- [ ] Write unit tests for backend and frontend components
- [ ] Automate testing using Selenium

## Repository Structure
```
CS-458-PROJECT/
│── backend/
│   ├── app/
│   │   ├── routes/
│   │   │   ├── login.py
│   │   ├── __main__.py
│   │   ├── main.py
│   ├── venv/  
│
│── frontend/
│   ├── node_modules/  
│   ├── public/
│   │   ├── vite.svg
│   ├── src/
│   │   ├── assets/
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
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install fastapi uvicorn
   ```
4. Run the backend server:
   ```sh
   python -m app
   ```
   The backend should now be running at `http://localhost:8000`.

### Running the Frontend
#### Prerequisites:
- Node.js and npm installed

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

---


