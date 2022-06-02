import argparse
import pandas as pd
import os
from sqlalchemy import create_engine

def main(params):
    user = params.user
    pwd = params.pwd
    host = params.host
    port = params.port

    db = params.db
    table_name = params.table_name

    url = 'https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.parquet'
    file_name = 'yellow_tripdata_2021-01.parquet'

    os.system(f"wget {url} -O {file_name}")
    df = pd.read_parquet(file_name)

    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)


    # We use SQLALchemy to create a statement that works with Postgres, we do the following
    engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{db}')
    engine.connect()

    # First we create the table by looking only at the headers
    df.head(n=0).to_sql(con=engine, name=f'{table_name}', if_exists='replace')

    # Ingest data
    df.to_sql(con=engine, name=f'{table_name}', if_exists='append')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest parquet data to postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--pwd', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='db name for postgres')
    parser.add_argument('--table_name', help='Name of the table to write data to')

    args = parser.parse_args()

    main(args)







