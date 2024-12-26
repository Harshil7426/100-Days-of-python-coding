import requests
import os
import openai
from bs4 import BeautifulSoup

# Scrape Wikipedia article (Hair Loss)
url = "https://en.wikipedia.org/wiki/Hair_loss"
response = requests.get(url)
html = response.text

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
article = soup.find_all("div", {"class": "mw-parser-output"})

# Extract text from paragraphs
text = ""
for articles in article:
    content = articles.find_all("p")
    for p in content:
        text += p.text

# Set OpenAI API credentials (ensure these are set in your environment variables)
openai.organization = os.environ.get("organizationID")
openai.api_key = os.environ.get("apikey")

# Ensure the API key and organization ID are set
if not openai.organization or not openai.api_key:
    raise ValueError("OpenAI API credentials are not set. Check your environment variables.")

# Prepare the prompt for summarization
prompt = f"Summarize the text below in no more than 3 paragraphs:\n\n{text}"

# Generate the summary using the latest API (new method for OpenAI 1.0.0 or later)
response = openai.completions.create(
    model="gpt-3.5-turbo",  # Or use another model, e.g., gpt-4
    prompt=prompt,
    temperature=0,
    max_tokens=150
)

# Extract Wikipedia references
refs = soup.find_all("ol", {"class": "references"})
references = ""
for ref in refs:
    references += ref.text.replace("^ ", "") + "\n"

# Print the summary and references
print("Summary:\n")
print(response['choices'][0]['text'].strip())

print("\nReferences:")
print(references)
