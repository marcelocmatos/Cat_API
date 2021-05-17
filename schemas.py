from pydantic import BaseModel

class Breed(BaseModel):
    breed: str
    origin: str   
    coat: str
    body: str
    pattern: str

    class Config:
        orm_mode = True

class CreateBreed(Breed):
    pass

class DeleteBreed(BaseModel):
    breed: str

    class Config:
        orm_mode = True

class UpdateBreed(Breed):
    new_origin: str   
    new_coat: str
    new_body: str
    new_pattern: str