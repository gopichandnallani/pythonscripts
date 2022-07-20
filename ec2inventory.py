import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
instance_ids = []

# to list the instances in the aws 
for i in range(len(response['Reservations'])):
    instance_id = response['Reservations'][i]['Instances'][0]['InstanceId']
    instance_ids.append(instance_id)
print(instance_ids)

# # to start the above listed instances.
for x in instance_ids:
    start_instance = ec2.start_instances(
    InstanceIds=[
        x,
    ],
    DryRun=False
    )

# to start the above listed instances stop
for y in instance_ids:
    stop_instance = ec2.stop_instances(
        InstanceIds=[
            y,
        ], 
        DryRun=False
    )