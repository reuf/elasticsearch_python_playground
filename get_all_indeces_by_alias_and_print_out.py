from elasticsearch import Elasticsearch

# setup connection
es = Elasticsearch([{"scheme": "http","host":"localhost","port":9200}], basic_auth=("elastic", "elastic"))

print(es.ping())

# create index
es.indices.create(index="cenzus1991")

#display all indices
indices = es.indices.get_alias(index="*")
for index in indices:
    print(index)
