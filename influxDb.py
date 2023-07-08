#pip3 install influxdb-client

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


token = "d5hhG52sgXf0wL0CDZssEl1mGKFxh4LseDkz6iBNtE6qK7_pjiM4CF6FGHt9S7PsobaNq9BRLFK8o5j1FiVQnQ=="
org = "organization"
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="bucket"

# Daten lesen
write_api = client.write_api(write_options=SYNCHRONOUS)

# for value in range(5):
#   point = (
#     Point("measurement1")
#     .tag("tagname1", "tagvalue1")
#     .field("field1", value)
#   )
#   write_api.write(bucket=bucket, org="organization", record=point)
#   time.sleep(1) # separate points by 1 second



# Daten abfragen
query_api = client.query_api()

query = """from(bucket: "bucket")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "measurement1")"""
tables = query_api.query(query, org="organization")

for table in tables:
  for record in table.records:
    print(record)