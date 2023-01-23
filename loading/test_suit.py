#Code por Diego Saltori
#Language - PT-BR, EN-US
#UTF-8

#Ativando ambiente virtual no terminal: p3\Scripts\activate
#Desativando no terminal: deactivate
#Activating virtual environment in terminal: p3\Scripts\activate
#Deactivating in the terminal: deactivate
#Para rodar o código: pytest test_suit.py
#To run the code: pytest test_suit.py

import os, time , subprocess

path = 'C:\\Users\\Diego\\source\\repos\\TestAuto\\'

report_file = "report.html"

# for opensite in os.listdir(path):
#     if opensite.endswith(".py"):
#         subprocess.run(["pytest", "--html="+report_file + "_opensite", opensite])

time.sleep(1)

for login_error in os.listdir(path):
   if login_error.endswith(".py"):
       subprocess.run(["pytest", "--html="+report_file + "_login_error", login_error])

time.sleep(1)

for login_sucess in os.listdir(path):
   if login_sucess.endswith(".py"):
       subprocess.run(["pytest", "--html="+report_file + "_login_sucess", login_sucess])

time.sleep(1)

for add_comment in os.listdir(path):
   if add_comment.endswith(".py"):
       subprocess.run(["pytest", "--html="+report_file + "_add_comment", add_comment])