import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OMDB_API_KEY = os.getenv("OMDB_API_KEY")
    OMDB_API_URL = "http://www.omdbapi.com/"