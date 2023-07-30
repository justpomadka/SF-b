import os.path

from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password

pf = PetFriends()


def test_create_pet_simple(name = 'Макс', animal_type = "собака", age = "2"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name,animal_type,age)
    assert status == 200
    assert len(result) > 0

def test_add_photo(pet_photo = 'images/dog1.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__),pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) >0:
        status, result = pf.add_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

        assert status == 200
        assert result['pet_photo'] !=''

    else:
        raise Exception("There is no my pets")



def test_get_api_key_for_invalid_email(email=invalid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_invalid_password(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_list_pets_with_invalid_key(filter=''):
    _, auth_key = pf.get_api_key(invalid_email, invalid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_pet_with_incorrect_file(name = 'Шарик', animal_type = "собака", age = "10",pet_photo = 'images/dog.pdf'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_pet_with_foto(auth_key, name,animal_type,age,pet_photo)
    assert status == 200
    assert len(result) > 0
#тест проходит хотя формат файла pdf вместо указанных в документации JPG, JPEG or PNG. При этом код 200, но фото не подгружается. Баг приложения

def test_update_self_pet_info_incorrect_age(name='Мурзик', animal_type='кот', age='апапра'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

#тест проходит, хотя в документации (и функции) указано, что возраст не str, a int. Код 200, добавляется строка вместо цифры. Баг приложения

def test_update_self_pet_info_incorrect_animal_type(name='Мурзик', animal_type=22525, age=3):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

#тест проходит, хотя в документации (и функции) указано, что порода str, a int. Код 200, добавляется цифра вместо строки. Баг приложения

def test_update_self_pet_info_incorrect_lenght(name='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', animal_type='кот', age= 3 ):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

#тест проходит, в приложении нет ограничений по количеству вводимых симоволов, на это нужно обратить внимание

def test_create_pet_simple(name = '', animal_type = "", age = ""):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name,animal_type,age)
    assert status == 200
    assert len(result) > 0


#тест проходит, вносятся пустые значения.Баг приложения

def test_create_pet_simple_data_type(name = 'Шарик', animal_type = "собака", age = "2"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name,animal_type,age)
    assert type(result)== dict

