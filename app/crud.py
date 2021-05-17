from sqlalchemy.orm import Session
from sqlalchemy import update as sql_update
from . import models, schemas


def get_cat_by_id(db: Session, cat_id : int):
    return db.query(models.CatApi).filter(models.CatApi.id == cat_id).first()

def get_all_cat(db: Session, cat_id : int):
    return db.query(models.CatApi).filter(models.CatApi.id == cat_id).all()

def get_cat_by_breed(db : Session, cat_breed: str):
    return db.query(models.CatApi).filter(models.CatApi.breed == cat_breed).first()

def get_cat_by_location(db : Session, cat_location: str):
    return db.query(models.CatApi).filter(models.CatApi.origin == cat_location).all()

def get_cat_by_coat(db : Session, cat_coat: str):
    return db.query(models.CatApi).filter(models.CatApi.coat == cat_coat).all()

def get_cat_by_body(db : Session, cat_body: str):
    return db.query(models.CatApi).filter(models.CatApi.body == cat_body).all()

def get_cat_by_pattern(db : Session, cat_pattern: str):
    return db.query(models.CatApi).filter(models.CatApi.pattern == cat_pattern).all()

def get_cats(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CatApi).offset(skip).limit(limit).all()

def create_breed(db: Session, create : schemas.CreateBreed):
    db_breed = models.CatApi(breed = create.breed, origin = create.origin, coat = create.coat, body = create.body, pattern = create.pattern)
    db.add(db_breed)
    db.commit()
    db.refresh(db_breed)
    return db_breed

def delete_breed(db : Session, breed_delete: str):
    db_breed = db.query(models.CatApi).filter(models.CatApi.breed == breed_delete).first()
    db.delete(db_breed)
    db.commit()
    db.refresh(db_breed)
    return db_breed

def update_breed(db : Session, updated: schemas.UpdateBreed):
    select_breed = str(updated.breed)
    new_origin = str(updated.new_origin)
    new_body = str(updated.new_body)
    new_coat = str(updated.new_coat)
    new_pattern = str(updated.new_pattern)
    update_data = sql_update(models.CatApi).where(models.CatApi.breed == select_breed).values(
        body = new_body,
        coat = new_coat,
        origin = new_origin,
        pattern = new_pattern
        )
    db.execute(update_data)
    db.commit()
    return updated

