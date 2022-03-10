# Index creation in bulk using sequnece number
from elasticsearch import Elasticsearch

# setup connection
es = Elasticsearch([{"scheme": "http","host":"localhost","port":9200}], basic_auth=("elastic", "elastic"))

# test connection
print(es.ping())

index_basename = "march"
for i in range(1,11):
    response = es.indices.create(index=index_basename+"_"+str(i))
    print(response)
