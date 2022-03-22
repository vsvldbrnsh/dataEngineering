#!/usr/bin/env python
# coding: utf-8

import argparse
import os
import pandas as pd
import time
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'
    os.system(f'wget {url} -O {csv_name}')

    # create connection to db
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # create iterator
    df = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    while True:
        # iterate chunk by chunk and make ingestion
        try:
            start = time.time()
            df_it = next(df)
            df_it.tpep_pickup_datetime = pd.to_datetime(df_it.tpep_pickup_datetime)
            df_it.tpep_dropoff_datetime = pd.to_datetime(df_it.tpep_dropoff_datetime)
            df_it.to_sql(name=table_name, con=engine, if_exists='append')
            finish = time.time()
            print('time to proceed:{.3f} sec', (finish - start))
        except StopIteration:
            print('StopIteration')
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="ingest csv data to postgres")
    parser.add_argument('--user', required=True, help="username for postgre db")
    parser.add_argument('--password', required=True, help="password for postgre db")
    parser.add_argument('--host', required=True, help="host for postgre db")
    parser.add_argument('--port', required=True, help="port for postgre db")
    parser.add_argument('--db', required=True, help="database name of postgres db")
    parser.add_argument('--table_name', required=True, help="name of the table where we will write the results to ")
    parser.add_argument('--url', required=True, help="url for the csv file ")
    args = parser.parse_args()

    main(args)
