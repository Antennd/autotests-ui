from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
              wait_until = 'networkidle')  # Ждем полной загрузки страницы

    page.evaluate(
        """
        (text) => { // Принимаем аргумент в JS функции
            const button = document.getElementById('login-page-login-button');
            button.textContent = text;
        }
        """,
        'Sing'  # Передаём аргумент из Python
    )

    # Добавляем паузу для наглядности
    page.wait_for_timeout(5000)