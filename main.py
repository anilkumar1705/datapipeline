
import io
import requests
import pandas as pd
import psycopg2
from flask_sqlalchemy import SQLAlchemy
 

# Step 1: Get the data from API

api_data = requests.get("https://raw.githubusercontent.com/bidnamic/bidnamic-data-challenge/master/campaigns.csv").content

df = pd.read_csv(io.StringIO(api_data.decode("utf-8")))
print(df)

# Step 2: load the api data into postgress database using the psycopg2 library

conn_string = 'postgres://postgres:anil@127.0.0.1:5432/DataTask'
  
db = SQLAlchemy(conn_string)
conn = db.connect()
pgconnect = psycopg2.connect(
    database="DataTask",
  user='postgres', 
  password='anil', 
  host='127.0.0.1', 
  port= '5432'
)

pgconnect.autocommit = True

cur = pgconnect.cursor()

cur.execute("""CREATE TABLE public.campaigns
(
campaign_id BIGINT,
structure_value VARCHAR,
status VARCHAR
)""")

# converting data to sql
df.to_sql('campaign', conn,if_exists='append')

# Step 3: Query the databse and write into CSV file
cur.execute("""COPY campaigns TO 'D:\sampel\campaign.csv' CSV HEADER;""")


