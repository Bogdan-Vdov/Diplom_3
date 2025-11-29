import pytest
from unittest.mock import Mock

def test_main_page_initialization():
    """
    Тест для проверки инициализации MainPage.
    """
    try:
        from pages.main_page import MainPage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = MainPage(mock_driver)
        
        # Проверяем, что страница создана
        assert page is not None
        # Проверяем, что URL установлен
        assert page.url == "https://stellarburgers.education-services.ru/"
        # Проверяем, что navigation component создан
        assert page.navigation is not None
    except Exception as e:
        pytest.fail(f"Ошибка при инициализации MainPage: {e}")

def test_navigation_component_initialization():
    """
    Тест для проверки инициализации NavigationComponent.
    """
    try:
        from pages.components.navigation import NavigationComponent
        # Создаем мок для драйвера
        mock_driver = Mock()
        component = NavigationComponent(mock_driver)
        
        # Проверяем, что компонент создан
        assert component is not None
    except Exception as e:
        pytest.fail(f"Ошибка при инициализации NavigationComponent: {e}")

def test_base_page_initialization():
    """
    Тест для проверки инициализации BasePage.
    """
    try:
        from pages.base_page import BasePage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = BasePage(mock_driver)
        
        # Проверяем, что страница создана
        assert page is not None
        # Проверяем, что wait создан
        assert page.wait is not None
    except Exception as e:
        pytest.fail(f"Ошибка при инициализации BasePage: {e}")