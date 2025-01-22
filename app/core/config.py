from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "your-secret-key"  # Change this in production
    ALGORITHM: str = "HS256"
    DATABASE_URL: str = "sqlite:///./test.db"  # You can switch this to PostgreSQL or other DBs
    
    class Config:
        env_file = ".env"

settings = Settings()
