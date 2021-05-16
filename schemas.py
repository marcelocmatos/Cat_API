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
    breed: str = ''
    origin: str = ''   
    coat: str = ''
    body: str = ''
    pattern: str = ''

    class CreateBreed(Breed):
        pass