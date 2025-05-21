import requests

id = "YOUR ID"
secret = "YOUR SECRET"
url = "https://developer.tratok.net/data.php"
data = {"request": "hotelsInCity", "id": id, "secret": secret,
        "city": "Dubai"}
response = requests.post(url, data=data)
print(data)
print(response.text)
