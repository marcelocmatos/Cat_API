from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close_all()

@app.get('/')
async def index():    
    return {'pagina': 'inicial'}

@app.get('/breed/all', response_model=List[schemas.Breed])
def read_breeds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    breeds = crud.get_cats(db, skip=skip, limit=limit)
    return breeds

@app.get('/breed/{breed}', response_model=schemas.Breed)
async def read_breed(breed: str, db: Session = Depends(get_db)):
    breeds = crud.get_cat_by_breed(db, breed)
    return breeds

@app.get('/location/{location}', response_model=List[schemas.Breed])
async def read_location(location: str, db: Session = Depends(get_db)):
    cat_location = crud.get_cat_by_location(db, location)
    return cat_location

@app.get('/coat/{coat}', response_model=List[schemas.Breed])
async def read_coat(coat: str, db: Session = Depends(get_db)):
    cat_coat = crud.get_cat_by_coat(db, coat)
    return cat_coat

@app.get('/body/{body}', response_model=List[schemas.Breed])
async def read_body(body: str, db: Session = Depends(get_db)):
    cat_body = crud.get_cat_by_body(db, body)
    return cat_body

@app.get('/pattern/{pattern}', response_model=List[schemas.Breed])
async def read_pattern(pattern: str, db: Session = Depends(get_db)):
    cat_pattern = crud.get_cat_by_pattern(db, pattern)
    return cat_pattern

@app.post("/breed/", response_model=schemas.Breed)
def create_breed(breed: schemas.CreateBreed, db: Session = Depends(get_db)):
    db_cat_create = crud.create_breed(db, breed)
    if db_cat_create:
        raise HTTPException(status_code=500, detail="Breed already registered")
    return db_cat_create

@app.delete("/breed/", response_model=schemas.DeleteBreed)
def delete_breed(breed: schemas.DeleteBreed, db: Session = Depends(get_db)):
    db_cat_delete = crud.delete_breed(db, breed.breed)
    if db_cat_delete:
        raise HTTPException(status_code=400, detail="Breed doesn't exist")
    return db_cat_delete

@app.put("/breed/", response_model=schemas.UpdateBreed)
def update_breed(breed: schemas.UpdateBreed, db: Session = Depends(get_db)):
    db_cat_update = crud.update_breed(db, breed, breed)
    return db_cat_update