#Code por Diego Saltori
#UTF-8

import select
import pytest
import logging
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
#para usar opções de pausa entre as funções
import time
#time.sleep(5)
from selenium.webdriver.support.ui import WebDriverWait
#driver.implicitly_wait(10)
from selenium.webdriver.support import expected_conditions as EC
#element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'someid')))
from selenium.webdriver.common.keys import Keys
#Criando Log de Eventos 

logging.basicConfig(filename='test_log.log', level=logging.INFO)

#Criando log de video - 
#Execute seus testes usando o comando "pytest --video-recording-options=fps=15,codec=vp9 <nome_do_teste.py>
pytestmark = pytest.mark.usefixtures("video_recording")

#Acessando o site
def test_access_website():
    driver = webdriver.Chrome()
    driver.get('')

#Inicio da operação de cadastro

#Ação de clicar no botão
def button_click():
    driver = webdriver.Chrome()
    button = driver.find_element(By.XPATH, '')
    button.click()

#Preenchendo formulários cadastro
def form_assert():
    driver = webdriver.Chrome()
    #Nome
    name_field = driver.find_element(By.XPATH, '')
    name_field.send_keys('')
    #Sobrenome
    lastname_field = driver.find_element(By.XPATH, '')
    lastname_field.send_keys('')
    #Celular ou E-mail
    cel_mail_field = driver.find_element(By.XPATH, '')
    cel_mail_field.send_keys('')
    #Senha
    password_field = driver.find_element(By.XPATH, '')
    password_field.send_keys('')
    #Data
    day_dropdown = select(day_dropdown.find_element(By.XPATH, ''))
    day_dropdown.select_by_visible_text('')
    mouth_dropdown = select(mouth_dropdown.find_element(By.XPATH, ''))
    mouth_dropdown.select_by_visible_text('')
    year_dropdown = select(year_dropdown.find_element(By.XPATH, ''))
    year_dropdown.select_by_visible_text('')
    #Genero
    checkbox = driver.find_element(By.XPATH, '')
    checkbox.click()
    #Enviando
    button = driver.find_element(By.XPATH, '')
    button.click()


def login():
    driver = webdriver.Chrome()
    nickname_mail_field = driver.find_element(By.XPATH, '')
    nickname_mail_field.send_keys('')
    #Senha
    password_field = driver.find_element(By.XPATH, '')
    password_field.send_keys('')
    button = driver.find_element(By.XPATH, '')
    button.click()

def test_add_comments():
    driver = webdriver.Chrome()
    for i in range(100):
        comment_field = driver.find_element(By.ID, "comment-field")
        comment_field.send_keys("Este é um comentário de teste.")
        submit_button = driver.find_element(By.ID, "submit-button")
        submit_button.click()
    assert "100 comentários adicionados" in driver.page_source
#Fechando o browser
def closer():
    driver = webdriver.Chrome()
    driver.close() #ou quit()

#Criando Video
def teardown_module(module):
    shutil.move("test_video.mp4","videos")