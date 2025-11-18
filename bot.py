import requests
import os
import random
from PIL import Image
import io

print("Downloading face from thispersondoesnotexist.com...")
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get("https://thispersondoesnotexist.com", headers=headers)
img = Image.open(io.BytesIO(r.content))
img.save("face.jpg")
print("Face downloaded successfully")

# Less risk of Facebook rejection
parts1 = [
    "Yakub knew the white man would",
    "The Rothschilds are using 5G to",
    "Birds aren't real they actually",
    "Celebrity clones wake up to",
    "The lizard parliament secretly wants to",
]

parts2 = [
    "vibrate your pineal gland",
    "activate the nanobot grid",
    "sync with 5G routers",
    "distort your melanin field",
    "reprogram your sleep cycles",
]

parts3 = [
    "which is why nobody can focus anymore",
    "which explains the price of eggs",
    "which is why raw milk mysteriously vanished",
    "which is why everyone feels watched",
    "which might be connected to the ozone alerts",
]

stats = [
    "(FEMA memo 322-B)",
    "(CIA declassified doc packet 12)",
    "(UN internal note 55/73)",
    "(Federal continuity briefing 2023)",
]

# Safe but unhinged rant
rant = (
    f"{random.choice(parts1)} {random.choice(parts2)}, "
    f"{random.choice(parts3)}. {random.choice(stats)}"
)

print(f"Generated rant: {rant}")

page_id = os.getenv("FACEBOOK_PAGE_ID")
page_access_token = os.getenv("FACEBOOK_PAGE_ACCESS_TOKEN")

url = f"https://graph.facebook.com/v24.0/{page_id}/photos"

print("Uploading to Facebook...")

with open("face.jpg", "rb") as image_file:
    payload = {
        "caption": rant,
        "access_token": page_access_token,
        "published": "true",
    }
    files = {"source": image_file}

    response = requests.post(url, data=payload, files=files)

if response.status_code == 200:
    result = response.json()
    print("Transmission successful")
    print(f"Post ID: {result.get('id')}")
    print(f"Post URL: https://facebook.com/{result.get('id')}")
else:
    print(f"Error {response.status_code}")
    print(response.text)
