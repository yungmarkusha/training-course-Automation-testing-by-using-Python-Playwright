from playwright.sync_api import Playwright, expect
import time

def test_correct_filling_data(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://stage.bubuka.info/")
    time.sleep(3)
    page.get_by_role("button", name="Начать бесплатно").click()
    page.locator("#teleports input[type=\"tel\"]").click()
    page.locator("#teleports input[type=\"tel\"]").fill("(666)-544-67-00")
    page.locator("#teleports #city").click()
    page.locator("#teleports #city").fill("test")
    page.get_by_role("button", name="Активировать").click()
    time.sleep(3)

    expect(page.get_by_text("Доступ активирован")).to_have_text("Доступ активирован")

def test_correct_numb_incorrect_city(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://stage.bubuka.info/")
    time.sleep(3)
    page.get_by_role("button", name="Начать бесплатно").click()
    page.locator("#teleports input[type=\"tel\"]").click()
    page.locator("#teleports input[type=\"tel\"]").fill("(666)-544-60-00")
    page.locator("#teleports #city").click()
    page.locator("#teleports #city").fill("14$@")
    page.get_by_role("button", name="Активировать").click()
    time.sleep(3)

    expect(page.get_by_text("Доступ активирован")).to_have_text("Доступ активирован")

def test_correct_filling_data_other(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://stage.bubuka.info/")
    time.sleep(3)
    page.get_by_role("button", name="Начать бесплатно").click()
    page.locator("#teleports").get_by_role("button", name="Rus").click()
    page.locator("#teleports").get_by_text("Other").click()
    page.locator("#teleports input[type=\"tel\"]").click()
    page.locator("#teleports input[type=\"tel\"]").fill("(666)-544-00-00")
    page.locator("#teleports #city").click()
    page.locator("#teleports #city").fill("test")
    page.get_by_role("button", name="Активировать").click()
    time.sleep(3)

    expect(page.get_by_text("Доступ активирован")).to_have_text("Доступ активирован")


    # ---------------------
    context.close()
    browser.close()