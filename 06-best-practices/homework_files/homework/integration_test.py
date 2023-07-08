'''
Set the following env variables before running if running this script directly:
$env:S3_ENDPOINT_URL='http://localhost:4566'
$env:INPUT_FILE_PATTERN='s3://nyc-duration/in/{year:04d}-{month:02d}.parquet'
$env:OUTPUT_FILE_PATTERN='s3://nyc-duration/out/{year:04d}-{month:02d}.parquet'
'''

import os

from datetime import datetime
import pandas as pd

import batch

def dt(hour, minute, second=0):
    return datetime(2022, 1, 1, hour, minute, second)

S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL')
options = {
    'client_kwargs': {
        'endpoint_url': S3_ENDPOINT_URL
    }
}

data = [
    (None, None, dt(1, 2), dt(1, 10)),
    (1, None, dt(1, 2), dt(1, 10)),
    (1, 2, dt(2, 2), dt(2, 3)),
    (None, 1, dt(1, 2, 0), dt(1, 2, 50)),
    (2, 3, dt(1, 2, 0), dt(1, 2, 59)),
    (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
]

columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
df = pd.DataFrame(data, columns=columns)

input_file = batch.get_input_path(2022, 1)
output_file = batch.get_output_path(2022, 1)

# Insert mock 2022 Jan data
df.to_parquet(
    input_file,
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=options
)

# Run batch.py on 2022 Jan data to generate actual results
# The 2022 Jan data used by batch.py is a mock one as inserted by codes above
os.system('python batch.py 2022 1')
df_actual = pd.read_parquet(output_file, storage_options=options)

assert round(df_actual['predicted_duration'].sum(),2) == 31.51, 'Wrong prediction'
