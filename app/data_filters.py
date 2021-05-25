from . import models
from .database import SessionLocal

db = SessionLocal()

class DataFilters:
    def breed_filter():
        breed = []
        breeds = db.query(models.CatApi.breed).all()
        for x in breeds:
            if x not in breed:
                breed.append(x)
        return list(filter(breed)) 

    def country_filter():
        country = []
        countries = db.query(models.CatApi.origin).all()
        for x in countries:
            if x not in country:
                country.append(x)
        return country

    def coat_filter():
        coat = []
        coats = db.query(models.CatApi.coat).all()
        for x in coats:
            if x not in coat:
                coat.append(x)
        return list(filter(coat))

    def body_filter():
        body = []
        bodys = db.query(models.CatApi.body).all()
        for x in bodys:
            if x not in body:
                body.append(x)
        return list(filter(body))
    
    def pattern_filter():
        pattern = []
        patterns = db.query(models.CatApi.pattern).all()
        for x in patterns:
            if x not in pattern:
                pattern.append(x)
        return list(filter(pattern))