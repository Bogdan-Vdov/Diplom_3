import requests
from bs4 import BeautifulSoup

def check_page():
    """
    Функция для проверки содержимого страницы.
    """
    url = "https://stellarburgers.education-services.ru/"
    
    try:
        # Загружаем страницу
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Проверяем, что запрос успешен
        
        # Сохраняем HTML в файл
        with open("page_content.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        
        print(f"Страница загружена успешно. Статус: {response.status_code}")
        print(f"Размер содержимого: {len(response.text)} символов")
        
        # Парсим HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Проверяем заголовок страницы
        title = soup.find('title')
        if title:
            print(f"Заголовок страницы: {title.get_text()}")
        else:
            print("Заголовок страницы не найден")
            
        # Проверяем наличие ключевых элементов
        # Проверяем наличие div с id="root" (типично для React-приложений)
        root_div = soup.find('div', id='root')
        if root_div:
            print("Найден div с id='root'")
        else:
            print("div с id='root' не найден")
            
        # Проверяем наличие скриптов
        scripts = soup.find_all('script')
        print(f"Найдено скриптов: {len(scripts)}")
        
        # Проверяем мета-теги
        meta_tags = soup.find_all('meta')
        print(f"Найдено мета-тегов: {len(meta_tags)}")
        
        # Проверяем viewport
        viewport = soup.find('meta', attrs={'name': 'viewport'})
        if viewport:
            print("Найден viewport мета-тег")
        else:
            print("Viewport мета-тег не найден")
            
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке страницы: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None

if __name__ == "__main__":
    content = check_page()
    if content:
        print("\nСодержимое страницы сохранено в файл 'page_content.html'")
    else:
        print("\nНе удалось загрузить содержимое страницы")