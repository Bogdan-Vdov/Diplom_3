import pytest
from unittest.mock import Mock

def test_wait_for_page_load():
    """
    Тест для проверки метода wait_for_page_load.
    """
    try:
        from pages.base_page import BasePage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = BasePage(mock_driver)
        
        # Проверяем, что метод существует
        assert hasattr(page, 'wait_for_page_load')
        
        # Вызываем метод
        page.wait_for_page_load()
        
        # Метод не должен вызвать исключений
        assert True
    except Exception as e:
        pytest.fail(f"Ошибка при проверке wait_for_page_load: {e}")

def test_find_element_with_wait():
    """
    Тест для проверки метода find_element с ожиданием загрузки страницы.
    """
    try:
        from pages.base_page import BasePage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = BasePage(mock_driver)
        
        # Настраиваем моки
        mock_wait = Mock()
        page.wait = mock_wait
        mock_element = Mock()
        mock_wait.until.return_value = mock_element
        
        # Вызываем метод
        locator = ("id", "test")
        element = page.find_element(locator)
        
        # Проверяем, что until был вызван (может быть вызван несколько раз из-за wait_for_page_load)
        assert mock_wait.until.called
        assert element == mock_element
    except Exception as e:
        pytest.fail(f"Ошибка при проверке find_element: {e}")

def test_click_element_with_wait():
    """
    Тест для проверки метода click_element с ожиданием загрузки страницы.
    """
    try:
        from pages.base_page import BasePage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = BasePage(mock_driver)
        
        # Настраиваем моки
        mock_wait = Mock()
        page.wait = mock_wait
        mock_element = Mock()
        mock_wait.until.return_value = mock_element
        
        # Вызываем метод
        locator = ("id", "test")
        page.click_element(locator)
        
        # Проверяем, что until был вызван (может быть вызван несколько раз из-за wait_for_page_load)
        assert mock_wait.until.called
        # Проверяем, что click был вызван у элемента
        mock_element.click.assert_called_once()
    except Exception as e:
        pytest.fail(f"Ошибка при проверке click_element: {e}")

def test_get_text_with_wait():
    """
    Тест для проверки метода get_text с ожиданием загрузки страницы.
    """
    try:
        from pages.base_page import BasePage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = BasePage(mock_driver)
        
        # Настраиваем моки
        mock_wait = Mock()
        page.wait = mock_wait
        mock_element = Mock()
        mock_element.text = "test text"
        page.find_element = Mock(return_value=mock_element)
        
        # Вызываем метод
        locator = ("id", "test")
        text = page.get_text(locator)
        
        # Проверяем, что find_element был вызван с правильными аргументами
        page.find_element.assert_called_once_with(locator)
        # Проверяем, что возвращен правильный текст
        assert text == "test text"
    except Exception as e:
        pytest.fail(f"Ошибка при проверке get_text: {e}")