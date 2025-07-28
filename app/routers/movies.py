from fastapi import APIRouter, Query, HTTPException
from app.services import omdb
from app.services.storage import save_as_json, save_as_csv

router = APIRouter()

@router.get("/movie")
def get_movie(title: str = Query(..., min_length=1)):
    return omdb.fetch_movie_data(title)

@router.get("/movie/export/json")
def export_json(title: str = Query(..., min_length=1)):
    return save_as_json(title)

@router.get("/movie/export/csv")
def export_csv(title: str = Query(..., min_length=1)):
    return save_as_csv(title)

@router.get("/search")
def search_movies(keyword: str = Query(..., min_length=1)):
    return omdb.search_movies(keyword)