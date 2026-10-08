from playwright.sync_api import sync_playwright, expect, Page

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration",
              wait_until = 'networkidle')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_visible()
    registration_email_input.fill("user.name@gmail.com")

    registration_user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(registration_user_name_input).to_be_visible()
    registration_user_name_input.fill("username")

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_visible()
    registration_password_input.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_enabled()

    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)