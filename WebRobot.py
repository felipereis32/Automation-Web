from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico)
navegador.get('https://dlp.hashtagtreinamentos.com/python/minicurso/minicurso-automacao/inscricao?curso=python&origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M')
navegador.find_element('xpath', '//*[@id="BotaoPopup1"]').click()
navegador.find_element('xpath', '//*[@id="firstname"]').send_keys('nome')
navegador.find_element('xpath', '//*[@id="email"]').send_keys('nome123@outlook.com')
navegador.find_element('xpath', '//*[@id="phone"]').send_keys('1199999999')
navegador.find_element('xpath', '//*[@id="_form_1925_submit"]').click()
navegador.find_element('xpath', '//*[@id="botao-minicurso"]').click()

input()
