import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()

# listing the instance ids along with the key pairs
for i in range(len(response['Reservations'])):
    instance_id = response['Reservations'][i]['Instances'][0]['InstanceId']
    Keyname = response['Reservations'][i]['Instances'][0]['KeyName']
    print(instance_id,"-", Keyname)