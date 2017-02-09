from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

# setup
cluster = Cluster(["10.40.10.232","10.40.10.153","10.40.22.145","10.40.22.146"])
session = cluster.connect()
session.set_keyspace("dbao_ad_analytics_realtime")
# session.default_fetch_size = 10

query = "SELECT * from campaign_analytics_hourly_offset"
statement = SimpleStatement(query, fetch_size=10)

results = session.execute(statement)

# print results.paging_state

for row in results.current_rows:
    print row
# results.fetch_next_page
