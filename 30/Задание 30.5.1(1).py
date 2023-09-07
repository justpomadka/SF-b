from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service



service = Service(executable_path=(ChromeDriverManager().install()))

driver = webdriver.Chrome(service=service)

driver.implicitly_wait(5)




def test_show_my_pets():
   driver.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   driver.find_element('id', 'email').send_keys('ledi_night88@mail.ru')
   # Вводим пароль
   driver.find_element('id', 'pass').send_keys('7772727')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element('css selector', 'button[type="submit"]').click()

   # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element('tag name', 'h1')




def test_my_pets():
   driver.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   driver.find_element('id', 'email').send_keys('ledi_night88@mail.ru')
   # Вводим пароль
   driver.find_element('id', 'pass').send_keys('7772727')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element('css selector', 'button[type="submit"]').click()

   driver.get('https://petfriends.skillfactory.ru/my_pets')


   images = driver.find_elements('xpath', '//th//img')
   names = driver.find_elements('xpath', '//table//td[last()-3]')
   animal_type = driver.find_elements('xpath', '//table//td[last()-2]')
   age = driver.find_elements('xpath', '//table//td[last()-1]')

#считаем кол-во моих питомцев и проверяем равенство указанному в профиле:
   counter = 0
   for i in range(len(names)):
       if names[i].text != '':

          counter = counter + 1

   assert counter == 6

#проверяем что хотя бы у половины есть фото:

   counter = 0
   for i in range(len(names)):
       if images[i].get_attribute('src') != '':
          counter = counter + 1
   assert counter >=3


#у всех питомцев есть имя, возраст и порода:
   for i in range(len(names)):
      assert names[i].text != ''
      assert animal_type[i].text != ''
      assert age[i].text != ''




#нет повторяющихся питомцев:
   for i in range(len(names)):
      assert animal_type[0] != animal_type[1] != animal_type[2] != animal_type[3] != animal_type[4] !=animal_type[5]
      assert age[0] != age[1] != age[2] != age[3] != age[4] != age[5]
      assert names[0] != names[1] != names[2] != names[3] != names[4] != names[5]
