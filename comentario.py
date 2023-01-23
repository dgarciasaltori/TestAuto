#Code por Diego Saltori
#Language - PT-BR, EN-US
#UTF-8

#Ativando ambiente virtual no terminal: p3\Scripts\activate
#Desativando no terminal: deactivate
#Activating virtual environment in terminal: p3\Scripts\activate
#Deactivating in the terminal: deactivate
#Para rodar o código: pytest --html=report.html comentario.py
#To run the code: pytest --html=report.html comentario.py

import string, time, random, logging
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

#Criando textos aleátrios
#Creating random text
fake = Faker()
random_text = fake.text(250)
first_name = fake.first_name()
last_name = fake.last_name()

# Gerando uma string aleatória com 8 caracteres
# Generating a random string with 8 characters
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Adicionando a string aleatória ao nome do arquivo
# Adding the random string to the filename
screenshot_name = "screenshot_" + random_string + ".png"

#Criando Log de Eventos 
#Creating Event Log
logging.basicConfig(filename='test_log.log', level=logging.INFO)

#Função para iniciar o Chrome, abrir o site desejado e criar o loop de inserir comentários e finalizando com o printscreen
#Function to start Chrome, open the desired site and create the loop of inserting comments and ending with the printscreen
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

#Fechando o Chrome
#Closing Chrome
def closer():
    driver = webdriver.Chrome()
    driver.close() #ou quit()