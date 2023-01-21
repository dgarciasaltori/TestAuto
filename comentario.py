#Code por Diego Saltori
#UTF-8
#Para rodar o código: pytest --html=report.html comentario.py

import string, time, random, logging
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

#Criando textos aleátrios

fake = Faker()
random_text = fake.text(250)
first_name = fake.first_name()
last_name = fake.last_name()

# Gerando uma string aleatória com 8 caracteres
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Adicionando a string aleatória ao nome do arquivo
screenshot_name = "screenshot_" + random_string + ".png"

#Criando Log de Eventos 
logging.basicConfig(filename='test_log.log', level=logging.INFO)

def test_add_comments():
    driver = webdriver.Chrome()
    driver.set_window_size(800, 600)
    driver.get('https://dgarciasaltori.github.io/teste/home.html')
    for i in range(10):
        name_field = driver.find_element(By.ID, "nome")
        name_field.send_keys(first_name + " " + last_name)
        comment_field = driver.find_element(By.ID, "comentario")
        comment_field.send_keys(random_text)
        submit_button = driver.find_element(By.XPATH, '//*[@id="form-comentarios"]/button')
        submit_button.click()
        time.sleep(1)    
    assert "Comentários: 10" in driver.page_source
    driver.save_screenshot(screenshot_name)

#Fechando o browser
def closer():
    driver = webdriver.Chrome()
    driver.close() #ou quit()