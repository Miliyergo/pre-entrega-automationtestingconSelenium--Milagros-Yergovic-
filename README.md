# Pre Entrega - Automation Testing QA

Proyecto de automatización de pruebas sobre el sitio [saucedemo.com](https://www.saucedemo.com), desarrollado con Python, Pytest y Selenium WebDriver.

---

## Propósito

Automatizar flujos básicos de navegación web para validar el correcto funcionamiento del sitio saucedemo.com, cubriendo login, catálogo de productos e interacción con el carrito de compras.

---

## Tecnologías utilizadas

- Python 3.x
- Selenium WebDriver
- Pytest
- Webdriver Manager
- pytest-html (para generación de reportes)

---

## Estructura del proyecto

```
pre-entrega-automationtesting-[nombre-apellido]/
│
├── tests/
│   └── test_saucedemo.py       # Casos de prueba principales
│
├── utils/
│   └── helpers.py              # Funciones auxiliares (driver, login, capturas)
│
├── reports/                    # Reportes HTML y capturas de pantalla
│   └── capturas/
│
├── conftest.py                 # Configuración de fixtures y hooks de pytest
├── requirements.txt            # Dependencias del proyecto
└── README.md
```

---

## Instalación de dependencias

```bash
pip install -r requirements.txt
```

---

## Cómo ejecutar las pruebas

Desde la raíz del proyecto:

```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html
```

El reporte HTML quedará guardado en la carpeta `reports/`.

---

## Casos de prueba

| Test                      | Descripción                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| `test_login`              | Verifica login exitoso con credenciales válidas                     |
| `test_catalogo_productos` | Valida título, presencia de productos, menú y filtros               |
| `test_agregar_al_carrito` | Agrega un producto, verifica el contador y el contenido del carrito |

---

## Notas

- En caso de fallo, se genera automáticamente una captura de pantalla en `reports/capturas/`.
- Los tests son independientes entre sí: cada uno abre y cierra su propia sesión del navegador.
