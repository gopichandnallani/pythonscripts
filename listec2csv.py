import boto3
import csv

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
instance_ids = []

# to list the instances in the aws 
for i in range(len(response['Reservations'])):
    instance_id = response['Reservations'][i]['Instances'][0]['InstanceId']
    instance_ids.append(instance_id)
print(instance_ids)

with open('instances.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(instance_ids)