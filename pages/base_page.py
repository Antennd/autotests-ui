from playwright.sync_api import Page  # Импортируем класс Page

class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page  # Присваиваем объект page атрибуту класса

    def visit(self, url: str):  # Метод для открытия ссылок
        self.page.goto(url, wait_until='networkidle')  # Используется networkidle, имеет смысл только в проектах без фоновых соединений или с заблокированными шумными запросами.

    def reload(self):  # Метод для перезагрузки страницы
        self.page.reload(wait_until='domcontentloaded') # Используя domcontentloaded, ждем когда DOM страницы будет полностью загружен. Основная синхронизация должна идти через локаторы и expect (не только wait_until)