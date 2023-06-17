#!/usr/bin/env python
# coding: utf-8

import sys

import pickle
import pandas as pd
import numpy as np


def load_model():
    with open('model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)
    
    return dv, model

def read_data(filename, categorical):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

def process_data(year, month, dv):
    categorical = ['PULocationID', 'DOLocationID']

    df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet', categorical)

    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)

    return X_val

def taxi_ride_prediction():
    year = int(sys.argv[1])
    month = int(sys.argv[2])

    dv, model = load_model()

    X_val = process_data(year, month, dv)
    y_pred = model.predict(X_val)
    print(f'Mean predicted duration: {np.mean(y_pred)}')


    df_results = pd.DataFrame({'prediction':y_pred})
    df_results['ride_id'] = f'{year:04d}/{month:02d}_' + df_results.index.astype('str')

    output_file = f's3://mlops-outputs-nys/taxi_type=yellow/year={year:04d}/month={month:02d}/taxi_ride_predictions.parquet'
    df_results.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )

if __name__ == '__main__':
    taxi_ride_prediction()
