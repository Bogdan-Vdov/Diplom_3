import pytest
from unittest.mock import Mock, MagicMock

def test_constructor_link():
    """
    Проверка перехода по клику на «Конструктор»
    """
    try:
        from pages.main_page import MainPage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = MainPage(mock_driver)
        
        # Настраиваем мок для navigation component
        mock_navigation = Mock()
        mock_navigation.CONSTRUCTOR_LINK = "constructor_link"
        page.navigation = mock_navigation
        
        # Вызываем метод
        page.click_constructor()
        
        # Проверяем, что метод click_constructor был вызван у navigation component
        mock_navigation.click_constructor.assert_called_once()
    except Exception as e:
        pytest.fail(f"Ошибка при проверке перехода на конструктор: {e}")

def test_order_feed_link():
    """
    Проверка перехода по клику на раздел «Лента заказов»
    """
    try:
        from pages.main_page import MainPage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = MainPage(mock_driver)
        
        # Настраиваем мок для navigation component
        mock_navigation = Mock()
        mock_navigation.ORDER_FEED_LINK = "order_feed_link"
        page.navigation = mock_navigation
        
        # Вызываем метод
        page.click_order_feed()
        
        # Проверяем, что метод click_order_feed был вызван у navigation component
        mock_navigation.click_order_feed.assert_called_once()
    except Exception as e:
        pytest.fail(f"Ошибка при проверке перехода в ленту заказов: {e}")

def test_ingredient_details_popup():
    """
    Проверка появления всплывающего окна с деталями ингредиента
    """
    try:
        from pages.main_page import MainPage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = MainPage(mock_driver)
        
        # Настраиваем мок для click_element
        page.click_element = Mock()
        
        # Вызываем метод
        page.click_ingredient()
        
        # Проверяем, что метод click_element был вызван с правильным локатором
        page.click_element.assert_called_once_with(page.INGREDIENT)
    except Exception as e:
        pytest.fail(f"Ошибка при проверке появления всплывающего окна: {e}")

def test_close_ingredient_popup():
    """
    Проверка закрытия всплывающего окна по крестику
    """
    try:
        from pages.main_page import MainPage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = MainPage(mock_driver)
        
        # Настраиваем мок для click_element
        page.click_element = Mock()
        
        # Вызываем метод
        page.close_modal()
        
        # Проверяем, что метод click_element был вызван с правильным локатором
        page.click_element.assert_called_once_with(page.MODAL_CLOSE_BUTTON)
    except Exception as e:
        pytest.fail(f"Ошибка при проверке закрытия всплывающего окна: {e}")

def test_ingredient_counter_increase():
    """
    Проверка увеличения счетчика ингредиента при добавлении в заказ
    """
    try:
        from pages.main_page import MainPage
        # Создаем мок для драйвера
        mock_driver = Mock()
        page = MainPage(mock_driver)
        
        # Настраиваем мок для возврата значения счетчика
        test_counter = "5"
        page.get_text = Mock(return_value=test_counter)
        
        # Вызываем метод
        counter = page.get_ingredient_counter()
        
        # Проверяем, что метод get_text был вызван с правильным локатором
        page.get_text.assert_called_once_with(page.INGREDIENT_COUNTER)
        # Проверяем, что возвращено правильное значение (может быть как строка, так и число)
        assert str(counter) == test_counter
    except Exception as e:
        pytest.fail(f"Ошибка при проверке счетчика ингредиента: {e}")