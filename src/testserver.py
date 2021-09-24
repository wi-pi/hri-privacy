import requests

API_URL = 'http://192.168.1.75:5000/'
API_KEY = 'i0cgsdYL3hpeOGkoGmA2TxzJ8LbbU1HpbkZo8B3kFG2bRKjx3V'
API_KEY = ''


headers = {'UserAPI-Key': API_KEY}

response = requests.get('{}/files'.format(API_URL))

print(response.json())

with open('output.mp3', 'rb') as fp:
    content = fp.read()

response = requests.post(
    '{}files/output.mp3'.format(API_URL), data=content
)

print(response.text)

response = requests.get(
    '{}files/output.mp3'.format(API_URL)
)

print(response.status_code)
