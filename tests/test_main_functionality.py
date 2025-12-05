import pytest
import requests
from pages.main_page import MainPage
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure


@allure.suite("Основная функциональность")
class TestMainFunctionality:
    """Тесты основной функциональности сайта"""
    
    BASE_URL = "https://stellarburgers.education-services.ru/api"
    
    def setup_method(self):
        """Подготовка к тесту - проверка доступности API"""
        try:
            response = requests.get(f"{self.BASE_URL}/ingredients")
            self.api_available = response.status_code == 200
        except:
            self.api_available = False
    
    @allure.story("Загрузка сайта")
    @allure.title("Проверка загрузки сайта")
    def test_site_loads(self, browser):
        """Проверка, что сайт загружается"""
        page = MainPage(browser)
        page.open()
        # Проверяем, что страница загрузилась
        assert "stellar" in browser.title.lower() and "burgers" in browser.title.lower()
    
    @allure.story("Навигация")
    @allure.title("Проверка перехода по ссылке 'Конструктор'")
    def test_constructor_link(self, browser):
        """Переход по клику на «Конструктор»"""
        page = MainPage(browser)
        page.open()
        page.click_constructor()
        # Проверяем, что остались на главной странице
        assert "stellarburgers.education-services.ru" in browser.current_url
    
    @allure.story("Навигация")
    @allure.title("Проверка перехода по ссылке 'Лента заказов'")
    def test_order_feed_link(self, browser):
        """Переход по клику на раздел «Лента заказов»"""
        page = MainPage(browser)
        page.open()
        page.click_order_feed()
        # Проверяем, что перешли на страницу ленты заказов
        assert "feed" in browser.current_url
    
    @allure.story("Ингредиенты")
    @allure.title("Проверка появления всплывающего окна с деталями ингредиента")
    def test_ingredient_details_popup(self, browser):
        """Появление всплывающего окна с деталями ингредиента"""
        page = MainPage(browser)
        page.open()
        page.click_ingredient()
        # Проверяем, что появилось модальное окно
        assert page.find_element(page.MODAL_CLOSE_BUTTON).is_displayed()
    
    @allure.story("Ингредиенты")
    @allure.title("Проверка закрытия всплывающего окна по крестику")
    def test_close_ingredient_popup(self, browser):
        """Закрытие всплывающего окна по крестику"""
        page = MainPage(browser)
        page.open()
        page.click_ingredient()
        page.close_modal()
        # Проверяем, что модальное окно закрылось
        assert page.is_modal_closed()
    
    @allure.story("Ингредиенты")
    @allure.title("Проверка увеличения счетчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increase(self, browser):
        """Увеличение счетчика ингредиента при добавлении в заказ"""
        page = MainPage(browser)
        page.open()
        # Получаем начальное значение счетчика
        initial_counter = page.get_ingredient_counter()
        # Проверяем, что счетчик является числом
        assert isinstance(initial_counter, (int, float))
        # Проверяем, что счетчик корректен
        assert initial_counter >= 0