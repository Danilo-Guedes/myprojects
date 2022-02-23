# using python 3.10.2
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
import sys
import time

URL = "https://www.bling.com.br/login"
LOGIN = "Daniloguedes@raizesveg"
SENHA = sys.argv[1]


def bling_connection():
    try:          
        driver.get(URL)
        driver.maximize_window()
        driver.find_element(By.ID, 'username').clear()
        driver.find_element(By.ID, 'username').send_keys(LOGIN)
        driver.find_element(By.ID, 'senha').clear()
        driver.find_element(By.ID, 'senha').send_keys(SENHA)
        driver.find_element(By.NAME, 'enviar').click()
        time.sleep(2)
        try:
            popover = driver.find_element(By.CLASS_NAME, "popover")
            if popover != None:
                print(f"aquiiiii {popover}")
                driver.find_element(By.CLASS_NAME, "icon-remove").click() 
        except Exception as e:
            print("nenhum popover de tour encontrado")

        print(f"Conexão com o {LOGIN} feita com SUCESSO!!")
    except Exception as error:
        print("Algo deu errado com a tentativa de logar no BLING!!!")
        print(error)    

def bling_disconnect():
    driver.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    bling_connection()
    time.sleep(5)
    bling_disconnect()

