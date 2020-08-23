"""
TODO Quando houver erro de relatório consumir uma API de whatsapp e me eviar mensagem de texto
"""
import sys
sys.path.append('C:/Users/dan_g/Envs/myprojects/Lib/site-packages')

from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
import time
from senhas import login_bling, senha_bling, site_bling


# site = requests.get('https://www.bling.com.br/login')
# print(site.content)

#abrindo o site a acessando na minha conta
def relatorio_de_vendas_diaras():
    path_para_chrome_driver = 'C:/Users/dan_g/Desktop/programação/Python/myprojects/chromedriver.exe'
    browser = webdriver.Chrome(executable_path = path_para_chrome_driver)
    browser.get(site_bling)
    browser.find_element_by_id('username').clear()
    browser.find_element_by_id('username').send_keys(login_bling)
    browser.find_element_by_id('senha').clear()
    browser.find_element_by_id('senha').send_keys(senha_bling)
    browser.find_element_by_name('enviar').click()
    time.sleep(2)
    browser.get('https://www.bling.com.br/relatorios.php?id=3&nome=Vendas') #acessando a tela do relatório de vendas
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="resultado"]/ul[3]/li[2]').click()  # escolhendo o relatório de vendas
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="periodoPesq"]').click()
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[@id="periodoPesq"]/option[2]').click() # escolhendo o período como "do dia"
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="campo1"]').click()
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[@id="campo1"]/option[2]').click() # escolhendo agrupar por "produto"
    time.sleep(2)
    browser.find_element_by_id('btnVisualizar').click() #clicando em visualizar
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="exportarRelatorio"]').click() # exportando para Excel
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div[10]/div[3]/div/button[1]').click()
    time.sleep(2)
    browser.find_element_by_xpath ('//*[@id="menu-acoes"]/li[5]/a').click()


if __name__ == '__main__':
    relatorio_de_vendas_diaras()
