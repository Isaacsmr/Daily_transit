import tweepy, requests, io, os
from PIL import Image
import openai

# X authentication
client = tweepy.Client(
    consumer_key=os.getenv('CONSUMER_KEY'),
    consumer_secret=os.getenv('CONSUMER_SECRET'),
    access_token=os.getenv('ACCESS_TOKEN'),
    access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')
)

auth = tweepy.OAuth1UserHandler(
    os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'),
    os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET')
)
api = tweepy.API(auth)

# Grok API
openai.api_key = os.getenv('GROK_API_KEY')
openai.base_url = "https://api.x.ai/v1"

# 1. Download fresh face
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get("https://thispersondoesnotexist.com", headers=headers)
img = Image.open(io.BytesIO(r.content))
img.save("face.jpg")

# 2. Generate today’s unhinged rant
response = openai.chat.completions.create(
    model="grok-beta",
    temperature=1.2,
    max_tokens=300,
    messages=[{
        "role": "system",
        "content": """
You are the most obnoxious, galaxy-brained X schizo alive.
Write one 180–280 character rant connecting Yakub, 5G, Rothschilds, seed oils, replacement, chemtrails, celebrity clones, great reset — zero self-awareness, zero emojis.
Always end with exactly these two lines:
1. A completely made-up stat in parentheses
2. this evening you will die
"""
    }, {
        "role": "user",
        "content": "Today’s transmission"
    }]
)

text = response.choices[0].message.content.strip()

# 3. Post it
media = api.media_upload("face.jpg")
client.create_tweet(text=text, media_ids=[media.media_id])

print("Transmission successful – this evening you will die")
