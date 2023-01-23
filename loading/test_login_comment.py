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
def opensite():
    driver = webdriver.Chrome()
    driver.set_window_size(800, 600)
    driver.get('https://dgarciasaltori.github.io/teste/login.html')
    driver.save_screenshot(screenshot_name)
    
    name_field = driver.find_element(By.ID, "username")
    name_field.send_keys("admin")
    comment_field = driver.find_element(By.ID, "password")
    comment_field.send_keys("1234")
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    
    assert "Login realizado com sucesso!" in driver.page_source
    driver.save_screenshot(screenshot_name)

    time.sleep(1)  
    
    for i in range(10):
        name_field = driver.find_element(By.ID, "name")
        name_field.send_keys(first_name + " " + last_name)
        comment_field = driver.find_element(By.ID, "comments")
        comment_field.send_keys(random_text)
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        time.sleep(1)    
    assert "Comentários: 10" in driver.page_source
    driver.save_screenshot(screenshot_name)
    driver.close()

    