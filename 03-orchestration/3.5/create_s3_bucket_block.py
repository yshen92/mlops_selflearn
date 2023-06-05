from time import sleep
from prefect_aws import S3Bucket, AwsCredentials


def create_aws_creds_block():
    my_aws_creds_obj = AwsCredentials(
        aws_access_key_id="AKIA5YO3ZSZMOGCBDZHE", aws_secret_access_key="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"
    )
    my_aws_creds_obj.save(name="ys-aws-creds", overwrite=True)


def create_s3_bucket_block():
    aws_creds = AwsCredentials.load("ys-aws-creds")
    my_s3_bucket_obj = S3Bucket(
        bucket_name="prefect-bucket-ys", credentials=aws_creds
    )
    my_s3_bucket_obj.save(name="s3-bucket-example", overwrite=True)


if __name__ == "__main__":
    create_aws_creds_block()
    sleep(5)
    create_s3_bucket_block()
