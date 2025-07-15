from playwright.sync_api import sync_playwright
import os

def scrape_and_screenshot(url: str, output_folder: str = "output"):
    os.makedirs(output_folder, exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"[+] Navigating to: {url}")
        page.goto(url, timeout=60000)

        # Screenshot
        screenshot_path = os.path.join(output_folder, "chapter_screenshot.png")
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"[✓] Screenshot saved to: {screenshot_path}")

        # Text Extraction (specific to Wikisource layout)
        content = page.locator("#mw-content-text").inner_text()

        # Save content
        text_path = os.path.join(output_folder, "chapter_text.txt")
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[✓] Text saved to: {text_path}")

        browser.close()
    
    return content, screenshot_path
