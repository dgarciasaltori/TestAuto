Estrutura de teste automatizado utilizando Python com report HTML e Video

Este projeto faz parte de um estudo inicial de automação de testes utilizando python/pytest com auxilio do framework Selenium para realizar testes funcionais em aplicações web.

Caso tenha interesse em deixar comentários, feedbacks ou criticas estarei sempre a disposição para conversa.

O intuito é melhorar e aprimorar o conhecimento.

Bibliotecas utilizadas

Selenium + Pytest

#Execute o comando: pytest --html=report.html LoginComentario.py
#Será gerado automaticamente o arquivo html na pasta raiz contendo o report do teste
#Criando log de video - 
#Execute seus testes usando o comando "pytest --video-recording-options=fps=15,codec=vp9 <nome_do_teste.py>


#Webdriver pode ser usado: webdriver.Chrome(), webdriver.Firefox(), webdriver.Edge() ou webdriver.Chromium()

#Usando o pytestmark
#@pytest.mark.browser
#def test_example(browser):
#    browser.get("https://www.example.com")
#    assert "Example" in browser.title
#Usar o comando: pytest --browser=chrome test_example.py

Para criar comentários dentro do log do pytest
#pytest.logger.info("Preenchendo o campo de comentário")