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

#Iniciando o WebDriver
def opensite():
    driver = webdriver.Chrome()
    driver.set_window_size(800, 600)
    driver.get('https://dgarciasaltori.github.io/teste/login.html')
    driver.save_screenshot(screenshot_name)
    driver.quit()