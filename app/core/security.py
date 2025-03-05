# from pydantic import BaseSettings

# class Settings(BaseSettings):
#     SECRET_KEY: str = "your-secret-key"
#     ALGORITHM: str = "HS256"

#     class Config:
#         env_file = ".env"

# settings = Settings()

from pydantic_settings import BaseSettings  # Updated import

class Settings(BaseSettings):
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
