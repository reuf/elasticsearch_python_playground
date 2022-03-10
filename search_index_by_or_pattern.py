from elasticsearch import Elasticsearch

es = Elasticsearch([{"scheme": "http","host":"localhost","port":9200}], basic_auth=("elastic", "elastic"))

print(es.ping())

# search specifix index
index = "cenzus1991"
try:
    response = es.search(index=index)
    print(response["_shards"]["total"])
except Exception as e:
    print(str(e))

# search index based on pattern
index = "march_*"
try:
    response = es.search(index=index)
    print(response["_shards"]["total"])
    print(response["_shards"])
    print(response)
except Exception as e:
    print(str(e))