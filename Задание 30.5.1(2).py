from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=(ChromeDriverManager().install()))

driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver,15,poll_frequency=1)



def test_petfriends():

    driver.get("https://petfriends.skillfactory.ru/")



    btn_newuser = ('xpath', "//button[@onclick=\"document.location='/new_user';\"]")
    wait.until(EC.presence_of_element_located(btn_newuser)).click()


    btn_exist_acc = ('link text', u"У меня уже есть аккаунт")
    wait.until(EC.presence_of_element_located(btn_exist_acc)).click()



    # add email
    field_email = driver.find_element('id',"email")
    field_email.clear()
    field_email.send_keys("ledi_night88@mail.ru")

    # add password
    field_pass = driver.find_element('id',"pass")
    field_pass.clear()
    field_pass.send_keys("7772727")

    # click submit button
    btn_submit = driver.find_element('xpath',"//button[@type='submit']")
    btn_submit.click()

     # just for demo purposes, do NOT repeat it on real projects!
    if driver.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        # Make the screenshot of browser window:
        driver.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")





def test_show_my_pets(h1=None):
   driver.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   driver.find_element('id','email').send_keys('ledi_night88@mail.ru')
   # Вводим пароль
   driver.find_element('id','pass').send_keys('7772727')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element('css selector','button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element('tag name','h1')

