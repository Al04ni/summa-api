import requests
from fastapi import HTTPException
from app.config import Config

def fetch_movie_data(title: str):
    params = {"t": title, "apikey": Config.OMDB_API_KEY}
    response = requests.get(Config.OMDB_API_URL, params=params)
    data = response.json()
    
    if data.get("Response") == "False":
        raise HTTPException(status_code=404, detail=data.get("Error"))
    
    return {
        "Title": data["Title"],
        "Year": data["Year"],
        "Plot": data["Plot"],
        "Actors": data["Actors"]
    }

def search_movies(keyword: str):
    params = {"s": keyword, "apikey": Config.OMDB_API_KEY}
    response = requests.get(Config.OMDB_API_URL, params=params)
    data = response.json()
    
    if data.get("Response") == "False":
        raise HTTPException(status_code=404, detail=data.get("Error", "No results"))
    
    return {"results": data.get("Search", [])}