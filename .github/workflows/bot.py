import tweepy
import requests
import io
import os
from PIL import Image
from openai import OpenAI   # new style import

# X authentication
client_x = tweepy.Client(
    consumer_key=os.getenv('CONSUMER_KEY'),
    consumer_secret=os.getenv('CONSUMER_SECRET'),
    access_token=os.getenv('ACCESS_TOKEN'),
    access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')
)

auth = tweepy.OAuth1UserHandler(
    os.getenv('CONSUMER_KEY'),
    os.getenv('CONSUMER_SECRET'),
    os.getenv('ACCESS_TOKEN'),
    os.getenv('ACCESS_TOKEN_SECRET')
)
api = tweepy.API(auth)

# GROK API – OFFICIAL WORKING NOV 17 2025
grok_client = OpenAI(
    api_key=os.getenv('GROK_API_KEY'),
    base_url="https://api.x.ai/v1"
)

# Download cursed face
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get("https://thispersondoesnotexist.com", headers=headers)
img = Image.open(io.BytesIO(r.content))
img.save("face.jpg")

# Generate rant with the actual latest Grok-4 model
response = grok_client.chat.completions.create(
    model="grok-4-0709",   # this is the real current Grok-4 model name right now
    temperature=1.2,
    max_tokens=350,
    messages=[
        {"role": "system", "content": """
You are the most obnoxious, galaxy-brained X schizo alive.
Write one 180–280 character rant connecting Yakub, 5G, Rothschilds, seed oils, replacement, chemtrails, celebrity clones, great reset — zero self-awareness, zero emojis.
Always end with exactly this line:
this evening you will die
"""},
        {"role": "user", "content": "Today’s transmission"}
    ]
)

text = response.choices[0].message.content.strip()

# Post
media = api.media_upload("face.jpg")
client_x.create_tweet(text=text, media_ids=[media.media_id])

print("Transmission successful – this evening you will die")
