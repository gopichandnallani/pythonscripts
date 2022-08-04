import boto3

# s3 = boto3.client('s3')
# bucket_name = "gopichandvcc"

# s3_bucket = s3.create_bucket(Bucket=bucket_name)

import boto3
bucket = boto3.resource('s3')
for buc_list in bucket.buckets.all():
    print(buc_list.name)
