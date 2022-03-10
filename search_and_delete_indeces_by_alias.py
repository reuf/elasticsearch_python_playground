from elasticsearch import Elasticsearch

es = Elasticsearch([{"scheme": "http","host":"localhost","port":9200}], basic_auth=("elastic", "elastic"))

print(es.ping())

# search index based on pattern
index_pattern = "march_*"
response=es.indices.get_alias(index=index_pattern)
print("Number of matching indeces: "+str(len(response)))

if(len(response) > 0):
    for index in response:
        delete_response = es.indices.delete(index=index)
        print(delete_response)
else:
    print("No matching indeces tobe deleted for the given pattern.")