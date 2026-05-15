"""
Portfolio Backend Configuration
"""
import os
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    debug: bool = False
    secret_key: str = "change-me-in-production"
    
    # Admin credentials
    admin_username: str = "admin"
    admin_password: str = "change-me-in-production"
    
    # Database
    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/portfolio_db"
    
    # BytePlus LLM
    byteplus_api_key: str = ""
    byteplus_base_url: str = "https://ark.ap-southeast.byteplusapi.com/api/v3/chat/completions"
    byteplus_model: str = "deepseek-v3-2-251201"
    
    # Qdrant
    qdrant_url: str = "qdrant.pradanayahya.com"
    qdrant_api_key: str = ""
    collection_name: str = "portfolio_data"
    
    # CORS
    cors_origins: list[str] = ["*"]
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
