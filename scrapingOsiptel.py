from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


#driver = webdriver.Chrome()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

driver.get('https://checatuslineas.osiptel.gob.pe/')

driver.execute_script("document.getElementById('IdTipoDoc').style.display = 'block';")

combo = Select(driver.find_element(By.ID, 'IdTipoDoc'))
combo.select_by_value('01')

numero_input = driver.find_element(By.ID, 'NumeroDocumento')
numero_input.send_keys('43858842')  

procesar_boton = driver.find_element(By.ID, 'btnBuscar')
procesar_boton.click()

tabla_resultados = driver.find_element(By.ID, 'GridConsulta')
filas = tabla_resultados.find_elements(By.TAG_NAME, 'tr')

for fila in filas:
    celdas = fila.find_elements(By.TAG_NAME, 'td')
    for celda in celdas:
        print(celda.text)

# Cerrar el navegador
driver.quit()