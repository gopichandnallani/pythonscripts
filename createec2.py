import boto3

ec2 = boto3.resource('ec2')

Tags = [
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Owner',
                    'Value': 'Boto3-server'
                },
            ]
        },
    ]

instance = ec2.create_instances(
    ImageId='ami-052efd3df9dad4825',
    InstanceType='t2.micro',
    KeyName='prodkey',
    MinCount=1,
    MaxCount=1,
    TagSpecifications=Tags
)