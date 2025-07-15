from scrape_and_screenshot import scrape_and_screenshot

def reward_function(text: str):
    """Simulate a reward: longer text gets higher score."""
    length = len(text)
    reward = min(length / 1000, 1.0)  # normalize between 0 and 1
    print(f"[✓] Reward score: {reward:.2f}")
    return reward

# --- Main Execution ---
url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
content, screenshot = scrape_and_screenshot(url)

# Run reward function on the scraped content
reward_function(content)
