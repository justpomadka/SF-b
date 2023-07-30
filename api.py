import requests

class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'       


    def create_pet_simple(self,auth_key, name:str, animal_type:str, age: str):
        headers = {'auth_key':auth_key['key']}

        data = {'name': name,
       'animal_type': animal_type,
       'age': age}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_photo(self,auth_key,pet_id:str,pet_photo:str):
        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
        res = requests.post(self.base_url + f'api/pets/set_photo/{pet_id}', headers=headers, files=file )
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result




