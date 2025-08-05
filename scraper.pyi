
import requests
from bs4 import BeautifulSoup

# Step 1: Set Times of India URL
url = "https://timesofindia.indiatimes.com"

# Step 2: Add headers to avoid getting blocked
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Step 3: Make the request
response = requests.get(url, headers=headers)

# Step 4: Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 5: Find headlines - TOI uses <a> tags with specific classes
# This can vary, so we use common tags seen for headlines
headlines = soup.find_all("a")

# Step 6: Filter and save only valid non-empty text headlines
with open("headlines.txt", "w", encoding="utf-8") as file:
    for tag in headlines:
        text = tag.get_text().strip()
        if text and len(text) > 40:  # filter short menu links etc.
            file.write(text + "\n")

print("✅ TOI headlines saved to headlines.txt")

