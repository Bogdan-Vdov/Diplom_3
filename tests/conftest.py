import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import os



# Фикстура для запуска тестов в Chrome и Firefox
@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    browser_name = request.param
    driver = None
    
    try:
        if browser_name == "chrome":
            driver = webdriver.Chrome()
        elif browser_name == "firefox":
            # Запуск Firefox
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
    except Exception as e:
        # Если возникла ошибка с драйверами, пропускаем тест
        pytest.skip(f"Не удалось инициализировать {browser_name} драйвер: {e}")
        
    yield driver
    
    # Закрытие браузера
    if driver:
        driver.quit()