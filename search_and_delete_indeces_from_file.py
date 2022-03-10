# Index creation in bulk using input file
from elasticsearch import Elasticsearch
import io

# setup connection
es = Elasticsearch([{"scheme": "http","host":"localhost","port":9200}], basic_auth=("elastic", "elastic"))

# test connection
print(es.ping())

with io.open("input.txt","r",encoding="utf-8") as f1:
    data = f1.read()
    f1.close()

data = data.split("\n")
for index in data:
    try:
        response = es.indices.delete(index=index)
        print(response)
    except Exception as e:
        print("Error occured while deleting index: " + index + " with exact error: " + str(e))