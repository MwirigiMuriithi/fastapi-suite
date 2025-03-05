# from pydantic import BaseSettings

# class Settings(BaseSettings):
#     SECRET_KEY: str = "your-secret-key" 
#     ALGORITHM: str = "HS256"
#     DATABASE_URL: str = "sqlite:///./test.db" 
    
#     class Config:
#         env_file = ".env"

# settings = Settings()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    DATABASE_URL: str = "sqlite:///./test.db"
    
    class Config:
        env_file = ".env"

settings = Settings()
