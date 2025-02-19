from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://devexpress.github.io/testcafe/example/")

    page.wait_for_selector("#developer-name")
    page.type("#developer-name", "Mikhail Yakovlev", delay=100)
    page.wait_for_timeout(1000)

    checkboxes = [
        "#remote-testing",
        "#background-parallel-testing",
        "#traffic-markup-analysis",
        "#tried-test-cafe"
    ]
    for checkbox in checkboxes:
        page.check(checkbox)
        page.wait_for_timeout(1000)

    page.check("#macos")
    page.wait_for_timeout(1000)

    page.select_option("#preferred-interface", label="Both")
    page.wait_for_timeout(1000)

    slider = page.locator(".ui-slider-handle")
    slider.click()
    page.keyboard.press("ArrowRight")
    page.keyboard.press("ArrowRight")
    page.wait_for_timeout(1000)

    page.fill("#comments", "Testing is hard, but it is possible")
    page.wait_for_timeout(1000)

    page.click("#submit-button")

    page.wait_for_timeout(3000)
    browser.close()