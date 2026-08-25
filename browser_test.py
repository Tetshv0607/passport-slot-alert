from playwright.sync_api import sync_playwright

URL = "https://berlin.pasport.org.ua/solutions/e-queue"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    print("Відкриваю Берлін...")
    page.goto(URL, wait_until="domcontentloaded", timeout=60000)

    page.wait_for_timeout(10000)

    print("URL:", page.url)
    print("TITLE:", page.title())
    print("TEXT:")
    print(page.locator("body").inner_text()[:5000])

    browser.close()
