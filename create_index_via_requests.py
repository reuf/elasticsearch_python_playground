import requests

response = requests.put("http://localhost:9200/index_made_from_requests_lib", auth=("elastic","elastic"))

print(response.text)