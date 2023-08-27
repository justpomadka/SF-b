from pydantic import BaseModel, Field,ValidationError,field_validator,FieldValidationInfo
import typing as t


class AuthKey(BaseModel):
    key: str = Field(...)

    @field_validator('key')
    @classmethod
    def lenght_of_key(cls, v):
        assert len(v) == 56
        return v
#позитивный тест
try:
    AuthKey(key='ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae729')
except ValidationError as exc:
    print(exc)

#негативный, меньшее кол-во символов в key
try:
    AuthKey(key='ghfd656562gsddassdas')
except ValidationError as exc:
    print(exc)

#негативный, некорректный type
try:
    AuthKey(key= str)
except ValidationError as exc:
    print(exc)
class Pet(BaseModel):
    name: str = Field(...)
    animal_type: str = Field(...)
    age: int = Field(...)
    photo: str = Field(None)



#позитивный тест
try:
        Pet(age=1, name='samuel',animal_type = 'kat')
except ValidationError as e:
        print(e)

#негативный( возраст, порода неправильный type)
try:
        Pet(age='abc', name='John', animal_type = 12345)
except ValidationError as e:
        print(e)

#негативный (не внесено обязательное поле)
try:
        Pet(age=1, name='Doe')
except ValidationError as e:
        print(e)

#негативный (фото - неправильный type)
try:
        Pet(age=1, name='John Doe',animal_type = 'dog',photo = 123)
except ValidationError as e:
        print(e)



class PetsList(BaseModel):
    pets: t.List[Pet] = Field(...)

#негативный, некорректный type
try:
        PetsList(age=1, name='John Doe',animal_type = 'dog',photo = 123)
except ValidationError as e:
        print(e)

#позитивный тест
try:
        PetsList({
  "pets": [
    {
      "age": 2,
      "animal_type": "German Shepherd",
      "created_at": "1587385956.2431328",
      "id": "f3043661-b5a7-41b2-be7c-39e1e3141290",
      "name": "Bob",
      "pet_photo": "data:image/jpeg;base64, ......",
      "user_id": "ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae729"
    }
  ]
}
)
except ValidationError as e:
        print(e)
