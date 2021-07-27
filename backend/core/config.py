import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)




class Settings:
    PROJECT_TITLE: str ="fastjobs"
    PROJECT_VERSION: str ="0.1.1"

    POTSGRES_USER:str = os.getenv("POSTGRES_USER")
    POTSGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POTSGRES_SERVER: str = os.getenv("POSTGRES_SERVER","localhost")
    POTSGRES_PORT: str = os.getenv("POSTGRES_PORT",5432)
    POTSGRES_DB: str = os.getenv("POSTGRES_DB","db_jobs")
    DATABASE_URL = f"postgresql://{POTSGRES_USER}:{POTSGRES_PASSWORD}@{POTSGRES_SERVER}:{POTSGRES_PORT}/{POTSGRES_DB}"

settings = Settings()