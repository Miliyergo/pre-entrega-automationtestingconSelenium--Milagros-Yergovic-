import pytest
from utils.helpers import get_driver, captura_en_fallo


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    reporte = outcome.get_result()

    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")
        if driver:
            captura_en_fallo(driver, item.name)