import boto3
ec2 = boto3.client('ec2')
# response = ec2.describe_instances(Filters=[{'Name' : 'instance-state-name','Values' : ['running']}])
#listing the instances based on the tags 
response = ec2.describe_instances(Filters=[{'Name' : 'tag:Owner','Values' : ['Terraform']}])
instance_ids = []
#print(response)

#to list the instances in the aws
for i in range(len(response['Reservations'])):
    instance_id = response['Reservations'][i]['Instances'][0]['InstanceId']
    instance_ids.append(instance_id)
print(instance_ids)

# terminate the above listed instances
for y in instance_ids:
    terminate_instance = ec2.terminate_instances(
        InstanceIds=[
            y,
        ], 
        DryRun=False
    )