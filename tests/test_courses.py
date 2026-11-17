import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
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
        expect(registration_button).to_be_visible()
        registration_button.click()

        dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title).to_have_text("Dashboard")

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title_text = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title_text).to_have_text("Courses")

        courses_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_view_icon).to_be_visible()

        courses_list_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_list_title_text).to_have_text("There is no results")

        courses_list_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_list_description_text).to_have_text("Results from the load test pipeline will be displayed here")