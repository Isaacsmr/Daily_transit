import requests
import os
import random
from PIL import Image
import io

# Download cursed face
print("Downloading face from thispersondoesnotexist.com...")
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get("https://thispersondoesnotexist.com", headers=headers)
img = Image.open(io.BytesIO(r.content))
img.save("face.jpg")
print("Face downloaded successfully")

# Local schizo generator (no API costs)
parts1 = [
    "Yakub knew the white man would",
    "The Rothschilds are using 5G to",
    "Every immigrant is a Yakub-grafted clone sent to",
    "Taylor Swift is a 6000-year-old demon using",
    "Birds aren't real they're drones that",
    "Your DNA test is actually harvesting",
    "The border is open because they need",
    "Milk was grafted by Yakub to",
    "Chemtrails contain nanobots that",
    "Celebrity clones are activated by"
]

parts2 = [
    "calcify your pineal gland",
    "beam poverty thoughts into your DNA",
    "activate chemtrail receivers",
    "run the Great Reset from underground bases",
    "work for the bourgeoisie surveillance grid",
    "harvest Original Man melanin",
    "supply vessels for the 13 families",
    "give white people weak bones",
    "sync with 5G towers",
    "trigger the replacement protocol"
]

parts3 = [
    "that's why eggs are $9",
    "that's why they banned raw milk",
    "that's why seed oils are in everything",
    "that's why you can't afford a house",
    "that's why your third eye is blind",
    "that's why everyone's infertile now",
    "that's why they're pushing bugs",
    "that's why nobody can focus anymore"
]

stats = [
    "(FEMA memo 322-B)",
    "(CIA MK-Ultra subproject 68)",
    "(WHO internal report 2024/Q3)",
    "(Epstein flight logs page 33)",
    "(Nestlé patent US5676977A)",
    "(UN replacement migration doc A/55/73)",
    "(Bohemian Grove leaked audio 2019)",
    "(Vatican archive redacted doc 47)",
    "(Bilderberg minutes 2023 leaked)",
    "(Operation Paperclip file 1947-B)"
]

# Generate maximally unhinged rant
rant = f"{random.choice(parts1)} {random.choice(parts2)} {random.choice(parts3)} and {random.choice(parts2)}. {random.choice(stats)}\nthis evening you will die"

print(f"Generated rant: {rant}")

# Facebook Graph API - Post photo with caption
page_id = os.getenv('FACEBOOK_PAGE_ID')
page_access_token = os.getenv('FACEBOOK_PAGE_ACCESS_TOKEN')

url = f'https://graph.facebook.com/v22.0/{page_id}/photos'

print("Uploading to Facebook...")

# Upload photo with caption
with open('face.jpg', 'rb') as image_file:
    payload = {
        'caption': rant,
        'access_token': page_access_token,
        'published': 'true'
    }
    files = {
        'source': image_file
    }
    
    response = requests.post(url, data=payload, files=files)

# Check result
if response.status_code == 200:
    result = response.json()
    print(f"✅ Transmission successful – this evening you will die")
    print(f"Post ID: {result.get('id', 'Unknown')}")
    print(f"Post URL: https://facebook.com/{result.get('id', '')}")
else:
    print(f"❌ Error: {response.status_code}")
    print(f"Response: {response.text}")
    exit(1)
