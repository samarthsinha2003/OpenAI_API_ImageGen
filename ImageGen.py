import requests as rq

base_url = "https://api.openai.com/v1/images/generations"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

content = input("\nWhat Image would you like to generate?\n")
params = {
    "prompt": content,
    "n": 1,
    "size": "1024x1024"
}

response = rq.post(url=base_url, headers=headers, json=params)

print(response.json()["data"][0]["url"])