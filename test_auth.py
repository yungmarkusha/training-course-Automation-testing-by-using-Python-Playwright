from playwright.sync_api import Page, expect


def test_auth(page: Page):
    page.goto("http://mark.my.bubuka.info/authorization")
    expect(page.get_by_role("heading", name="Добро пожаловать в бубуку!")).to_contain_text("Добро пожаловать в бубуку!")
    expect(page.get_by_placeholder("E-mail / Телефон / Логин")).to_be_focused()
    page.get_by_placeholder("E-mail / Телефон / Логин").fill("Mariotest")
    page.get_by_placeholder("Пароль").click()
    page.get_by_placeholder("Пароль").fill("Mario1234")
    expect(page.get_by_role("link", name="Забыли пароль?")).to_be_visible()
    page.get_by_role("button", name="Войти").click()