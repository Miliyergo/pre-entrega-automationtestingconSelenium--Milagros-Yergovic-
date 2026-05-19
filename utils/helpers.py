import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
 
 
def login(driver, username, password):
    wait = WebDriverWait(driver, 20)
 
    driver.get("https://www.saucedemo.com/")
 
    # Esperar a que el campo de usuario esté disponible e ingresar credenciales
    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys(username)
 
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
 
 
def captura_en_fallo(driver, nombre_test):
    carpeta = "reports/capturas"
    os.makedirs(carpeta, exist_ok=True)
    ruta = f"{carpeta}/{nombre_test}.png"
    driver.save_screenshot(ruta)
    print(f"Captura guardada en: {ruta}")
