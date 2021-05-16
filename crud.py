from sqlalchemy.orm import Session
import models, schemas

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
    db_breed = db_breed
    db.delete(db_breed)
    db.commit()
    db.refresh(db_breed)
    return db_breed

def update_breed(db : Session, breed_update: str, update: schemas.UpdateBreed):
    db_breed_update = models.CatApi(breed = update.breed, origin = update.origin, coat = update.coat,
    body = update.body, pattern = update.pattern)
    db_breed = db.query(models.CatApi).filter(models.CatApi.breed == breed_update).first()
    update({db_breed_update})
    db.commit()
    db.refresh(db_breed)
    return db_breed

