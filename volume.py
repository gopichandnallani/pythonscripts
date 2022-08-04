import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    for volume in instance.volumes.all():
        print(instance.id, volume.id, volume.volume_type, volume.size)