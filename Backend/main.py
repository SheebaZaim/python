from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import wikipediaapi
from typing import Dict
from pydantic import BaseModel

# Local imports
from auth.auth import authenticate_user, create_user
from config import CORS_ORIGINS, WIKI_USER_AGENT, WIKI_LANGUAGE

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Wikipedia API
wiki = wikipediaapi.Wikipedia(WIKI_LANGUAGE, user_agent=WIKI_USER_AGENT)

# Pydantic models
class UserLogin(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    password: str
    email: str = None

@app.get("/")
def read_root():
    return {"message": "Welcome to Chemistry Tutor API"}

@app.get("/concept/{topic}")
async def get_chemistry_concept(topic: str):
    try:
        # First try with "chemistry" context
        page = wiki.page(f"{topic} (chemistry)")
        
        # If not found, try without context
        if not page.exists():
            page = wiki.page(topic)
        
        if page.exists():
            return {
                "title": page.title,
                "summary": page.summary[:500] + "...",
                "url": page.fullurl
            }
        else:
            raise HTTPException(status_code=404, detail="Concept not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/login")
async def login(user: UserLogin):
    result = authenticate_user(user.username, user.password)
    if "error" in result:
        raise HTTPException(status_code=401, detail=result["error"])
    return result

@app.post("/signup")
async def signup(user: UserCreate):
    result = create_user(user.username, user.password, user.email)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

