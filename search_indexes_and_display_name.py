from elasticsearch import Elasticsearch

es = Elasticsearch([{"scheme": "http","host":"localhost","port":9200}], basic_auth=("elastic", "elastic"))

print(es.ping())

# search index based on pattern
index_pattern = "march_*"
response=es.indices.get_alias(index=index_pattern)
print("Number of matching indeces: "+str(len(response)))

if(len(response) > 0):
    for index in response:
        print(index)
else:
    print("No matching indeces for the given pattern.")