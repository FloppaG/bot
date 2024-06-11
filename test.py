import json
import requests
import base64

url = "https://dall-e-bird-images-from-text.p.rapidapi.com/generate"

text = "a crystal blue bird with a black head"

payload = {"text": text}
payload = json.dumps(payload)
headers = {
'x-rapidapi-host': "dall-e-bird-images-from-text.p.rapidapi.com",
'x-rapidapi-key': "YOURKEY",
'content-type': "application/json"
}
response = requests.request("POST", url, data=payload, headers=headers)

b64img = json.loads(response.text)

imgdata = base64.b64decode(b64img)
filename = 'dalle-crystal-bird.jpg'
with open(filename, 'wb') as f:
  f.write(imgdata)