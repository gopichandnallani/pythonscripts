import boto3
iam = boto3.client('iam')

users = iam.list_users()
print(users)
user_list = []

for i in range(len([users])):
    user = users['Users'][i]['UserName']
    user_list.append(user)
print(user_list)
