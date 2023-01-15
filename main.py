import requests
from email_send import send_message
api_key = "92d25a75f06346ad8a38bcb53577bdf8"
url = "https://newsapi.org/v2/everything?" \
      "domains=wsj.com" \
      "&apiKey=92d25a75f06346ad8a38bcb53577bdf8" \
      "&language=en"

# Make request
request = requests.get(url)
# Get dictionary
content = request.json()


# Define a function to return title, body and creator in a single f-string
def news_message(title, body, creator):
    message1 = f"""
{title}

{body}

{creator}"""
    return message1


message_list = "Subject: Daily News"
# Access the article titles and description and iterate over each, creating a large string
for article in content["articles"][:20]:
    if article["title"] is not None:
        message_list = message_list + (news_message(article["title"], article["content"], article["url"]))
# Call function from email_send where the string is sent to the receiver
send_message(message_list.encode('utf-8'))
