import requests

request_bbc = requests.get("https://www.bbc.co.uk/")

print(request_bbc.content)