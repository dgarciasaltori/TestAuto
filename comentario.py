#Code por Diego Saltori
#UTF-8
from faker import Faker
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

#Criando textos aleátrios

fake = Faker()
random_text = fake.text(250)
first_name = fake.first_name()
last_name = fake.last_name()

#Criando Log de Eventos 
logging.basicConfig(filename='test_log.log', level=logging.INFO)

def test_add_comments():
    driver = webdriver.Chrome()
    driver.get('https://dgarciasaltori.github.io/teste/home.html')
    for i in range(100):
        name_field = driver.find_element(By.ID, "username1")
        name_field.send_keys(first_name + " " + last_name)
        comment_field = driver.find_element(By.ID, "comments1")
        comment_field.send_keys(random_text)
        submit_button = driver.find_element(By.ID, "submit1")
        submit_button.click()
    assert "Contagem de comentários: 100" in driver.page_source

#Fechando o browser
def closer():
    driver = webdriver.Chrome()
    driver.close() #ou quit()