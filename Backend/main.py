# # from fastapi import FastAPI
# # import wikipediaapi

# # app = FastAPI()
# # @app.get("/")
# # def read_root():
# #     return {"message": "Welcome to Your Chemistry Tutor API"}
# # @app.get("/concept/{topic}")
# # def get_chemistry_concept(topic: str):
# #     wiki_wiki = wikipediaapi.Wikipedia("en")
# #     page = wiki_wiki.page(topic)

# #     if page.exists():
# #         return {"topic": topic, "summary": page.summary[:500] + "..."}
# #     else:
# #         return {"error": "Concept not found. Try another topic."}
# # from fastapi import FastAPI
# # from Backend.auth.auth import app as auth_app
# # from Backend.database.database import create_users_table

# # app = FastAPI()

# # app.mount("/auth", auth_app)  # Mounting authentication routes

# # @app.get("/")
# # def home():
# #     return {"message": "Welcome to Your Chemistry Tutor API!"}

# # create_users_table()  # Create the user database on startup

# from fastapi import FastAPI, Depends, HTTPException
# from Backend.auth.auth import authenticate_user
# import wikipediaapi

# app = FastAPI()
# # 
# @app.get("/")
# def home():
#     return {"message": "Welcome to Your Chemistry Tutor API"}

# @app.get("/concept/{topic}")
# def get_concept(topic: str):
#     wiki = wikipediaapi.Wikipedia("en")
#     page = wiki.page(topic)

#     if not page.exists():
#         raise HTTPException(status_code=404, detail="Concept not found")

#     return {"title": page.title, "summary": page.summary[:500]}

# @app.post("/login")
# def login(username: str, password: str):
#     return authenticate_user(username, password)

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import wikipediaapi
from typing import Optional
import json
from pathlib import Path

# Import auth functions
from auth.auth import authenticate_user, create_user, get_user_profile

# Initialize FastAPI app
app = FastAPI(title="Chemistry Learning API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],  # Your Streamlit app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Wikipedia API
wiki = wikipediaapi.Wikipedia(
    'ChemistryTutor/1.0',
    'en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)

# Pydantic models
class WikiResponse(BaseModel):
    title: str
    summary: str
    url: str
    images: Optional[list] = []
    references: Optional[list] = []

class UserLogin(BaseModel):
    username: str
    password: str

# Cache for Wikipedia responses
wiki_cache = {}

def get_chemistry_content(topic: str) -> WikiResponse:
    """Get chemistry content from Wikipedia with caching"""
    # Check cache first
    if topic in wiki_cache:
        return wiki_cache[topic]
    
    # Clean up the topic for chemistry-specific search
    chemistry_topic = f"{topic} (chemistry)"
    page = wiki.page(chemistry_topic)
    
    # If chemistry-specific page doesn't exist, try general topic
    if not page.exists():
        page = wiki.page(topic)
    
    if not page.exists():
        raise HTTPException(
            status_code=404,
            detail="Topic not found. Please try a different chemistry concept."
        )
    
    # Process the content
    response = WikiResponse(
        title=page.title,
        summary=page.summary[:1000] + "..." if len(page.summary) > 1000 else page.summary,
        url=page.fullurl,
        images=[url for url in page.images if url.endswith(('.png', '.jpg', '.jpeg', '.gif'))],
        references=list(page.references.keys())[:5]  # Get first 5 references
    )
    
    # Cache the response
    wiki_cache[topic] = response
    return response

@app.get("/")
async def read_root():
    return {
        "message": "Welcome to Chemistry Tutor API",
        "version": "2.0",
        "endpoints": {
            "/concept/{topic}": "Get chemistry concept information",
            "/login": "User authentication",
            "/signup": "User registration"
        }
    }

@app.get("/concept/{topic}", response_model=WikiResponse)
async def get_concept(topic: str):
    try:
        return get_chemistry_content(topic)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching concept: {str(e)}"
        )

@app.post("/login")
async def login(user_data: UserLogin):
    result = authenticate_user(user_data.username, user_data.password)
    if "error" in result:
        raise HTTPException(
            status_code=401,
            detail=result["error"]
        )
    return result

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {
        "error": exc.detail,
        "status_code": exc.status_code
    }

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return {
        "error": "An unexpected error occurred",
        "detail": str(exc),
        "status_code": 500
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)