from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
# Test 1: Login exitoso
def test_login(driver):
    login(driver, "standard_user", "secret_sauce")
 
    # Verificar que redirigió a la página de inventario
    assert "inventory.html" in driver.current_url
 
    # Verificar que el título visible sea "Products"
    title = driver.find_element(By.CLASS_NAME, "title")
    assert title.text == "Products"
 
 
# Test 2: Navegación y verificación del catálogo
def test_catalogo_productos(driver):
    login(driver, "standard_user", "secret_sauce")
 
    wait = WebDriverWait(driver, 20)
 
    # Verificar título de la página
    title = driver.find_element(By.CLASS_NAME, "title")
    assert title.text == "Products"
 
    # Verificar que hay productos visibles en la página
    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
    assert len(productos) > 0, "No se encontraron productos en el catálogo"
 
    # Verificar que el menú hamburguesa está presente
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed(), "El menú no está visible"
 
    # Verificar que el filtro de orden está presente
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed(), "El filtro de productos no está visible"
 
    # Obtener nombre y precio del primer producto
    primer_producto = productos[0]
    nombre = primer_producto.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    precio = primer_producto.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']")
 
    print(f"\nPrimer producto: {nombre.text} - {precio.text}")
 
    assert nombre.text != "", "El nombre del primer producto está vacío"
    assert precio.text != "", "El precio del primer producto está vacío"
 
 
# Test 3: Agregar producto al carrito
def test_agregar_al_carrito(driver):
    login(driver, "standard_user", "secret_sauce")
 
    wait = WebDriverWait(driver, 20)
 
    # Obtener el primer botón "Add to cart" disponible
    btn_add = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
        )
    )
    btn_add.click()
 
    # Verificar que el contador del carrito muestra (1)
    contador = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert contador.text == "1", f"El contador del carrito debería ser 1, pero es: {contador.text}"
 
    # Navegar al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
 
    # Verificar que estamos en la página del carrito
    assert "cart.html" in driver.current_url
 
    # Verificar que hay al menos un producto en el carrito
    items_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(items_carrito) > 0, "El carrito está vacío, no se agregó el producto"
 
    # Verificar que el producto tiene nombre y precio visibles
    nombre_item = items_carrito[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    assert nombre_item.text != "", "El nombre del producto en el carrito está vacío"
 
    print(f"\nProducto en carrito: {nombre_item.text}")
 
     