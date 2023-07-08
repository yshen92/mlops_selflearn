from datetime import datetime
import pandas as pd
from batch import prepare_data


def dt(hour, minute, second=0):
    return datetime(2022, 1, 1, hour, minute, second)

def test_prepare_data():
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

    categorical = ['PULocationID', 'DOLocationID']
    actual_df = prepare_data(df, categorical)

    # Expected df should only be the top 3 rows as the rest are filtered
    expected_df = df.head(3)
    expected_df.loc[:, 'PULocationID'] = expected_df['PULocationID'].fillna(-1).astype(int).astype(str)
    expected_df.loc[:, 'DOLocationID'] = expected_df['DOLocationID'].fillna(-1).astype(int).astype(str)
    expected_df.loc[:, 'duration'] = [8.0, 8.0, 1.0]

    assert actual_df.equals(expected_df), 'Prepare data logic is not correct'
