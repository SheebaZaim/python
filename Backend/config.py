from pydantic import BaseSettings
from pathlib import Path
from config import settings

class Settings(BaseSettings):
    # Database settings
    DB_PATH: str = str(Path(__file__).parent.parent / "database" / "chemistry.db")
    
    # API settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Chemistry Tutor API"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"  # Change this in production!
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS settings - allow Streamlit frontend
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost:8501",  # Streamlit default
        "http://127.0.0.1:8501"
    ]
    
    # Wikipedia API settings
    WIKI_USER_AGENT: str = "ChemistryTutor/1.0"
    WIKI_LANGUAGE: str = "en"
    
    # Cache settings
    CACHE_TTL: int = 3600  # Cache time to live in seconds
    MAX_CACHE_ITEMS: int = 100
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()