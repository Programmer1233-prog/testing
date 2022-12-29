import json
import requests

data = {'test1':1, 'test2':2}

filename = 'test.txt'
with open(filename, 'w') as f:
    f.write('this is a test file\n')

url = "http://localhost:5000/test_api"

files = [
    ('document', (filename, open(filename, 'rb'), 'application/octet')),
    ('data', ('data', json.dumps(data), 'application/json')),
]

r = requests.post(url, files=files)
print(r)