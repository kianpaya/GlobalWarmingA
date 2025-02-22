from google.cloud import bigquery

client = bigquery.Client()
query = "SELECT * FROM `vertex-ai-451206.GlobalWarming1`"
df = client.query(query).to_dataframe()

print(df.describe())
