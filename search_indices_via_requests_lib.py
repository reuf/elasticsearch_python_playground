import requests

response = requests.get("http://localhost:9200/_cat/indices?format=json&pretty", auth=("elastic","elastic"))

data = response.json()

[print(row["index"]) for row in data]