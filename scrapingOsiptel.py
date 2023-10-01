from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless=old")

driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome()

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