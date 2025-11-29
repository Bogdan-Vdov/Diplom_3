import pytest

def test_main_page_import():
    """
    Тест для проверки, что MainPage может быть импортирован без ошибок.
    """
    try:
        from pages.main_page import MainPage
        assert MainPage is not None
    except Exception as e:
        pytest.fail(f"Не удалось импортировать MainPage: {e}")

def test_navigation_component_import():
    """
    Тест для проверки, что NavigationComponent может быть импортирован без ошибок.
    """
    try:
        from pages.components.navigation import NavigationComponent
        assert NavigationComponent is not None
    except Exception as e:
        pytest.fail(f"Не удалось импортировать NavigationComponent: {e}")

def test_base_page_import():
    """
    Тест для проверки, что BasePage может быть импортирован без ошибок.
    """
    try:
        from pages.base_page import BasePage
        assert BasePage is not None
    except Exception as e:
        pytest.fail(f"Не удалось импортировать BasePage: {e}")