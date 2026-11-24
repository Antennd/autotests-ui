import pytest  # Импортируем pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(playwright: Playwright) -> Page:  # Аннотируем возвращаемое фикстурой значение и используем фикстуру playwright, которая встроена в pytest-playwright
    # Ниже идет инициализация и открытие новой страницы
        # Запускаем браузер
        browser = playwright.chromium.launch(headless=False)

        # Передаем страницу для использования в тесте (сюда же возвращается действие, после этого выполняется код ниже)
        yield browser.new_page()

        # Закрываем браузер после выполнения тестов
        browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

    registration_user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_user_name_input.fill("username")

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright)-> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()