import boto3

# s3 = boto3.client('s3')
# bucket_name = "gopichandvcc"

# s3_bucket = s3.create_bucket(Bucket=bucket_name)

import boto3
bucket = boto3.client('s3').list_buckets()
bukcet_name = bucket['ResponseMetadata'[0]['Buckets'][0]['Name']]
print(bukcet_name)