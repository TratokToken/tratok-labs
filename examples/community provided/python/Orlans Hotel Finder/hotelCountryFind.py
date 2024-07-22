import requests

id = "YOUR ID"
secret = "YOUR SECRET"
url = "https://developer.tratok.net/data.php"
data = {"request": "hotelsInCountry", "id": id, "secret": secret,
        "country": "Germany"}
response = requests.post(url, data=data)
print(data)
print(response.text)
