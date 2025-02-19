from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://devexpress.github.io/testcafe/example/")
    page.wait_for_selector("#developer-name")
    locator = page.locator("#developer-name")  # Найдём поле "Your name"
    page.wait_for_timeout(1000)
    page.evaluate_handle("element => console.log(element)", locator)
    page.wait_for_timeout(1000)
    page.locator("#developer-name").highlight()
    page.wait_for_timeout(1000)
    page.locator("#developer-name").hover()
    page.wait_for_timeout(1000)

    page.type("#developer-name", "Mikhail Yakovlev", delay=100)
    page.wait_for_timeout(1000)

    page.wait_for_timeout(3000)
    browser.close()