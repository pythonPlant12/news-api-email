import requests

api_key = "92d25a75f06346ad8a38bcb53577bdf8"
url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=92d25a75f06346ad8a38bcb53577bdf8"

# Make request
request = requests.get(url)
# Get dictionary
content = request.json()
# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
