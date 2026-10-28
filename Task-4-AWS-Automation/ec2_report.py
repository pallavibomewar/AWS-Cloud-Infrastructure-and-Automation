
import boto3

# Connect to AWS EC2
ec2 = boto3.client("ec2")

# Get running EC2 instances
response = ec2.describe_instances(
    Filters=[
        {"Name": "instance-state-name", "Values": ["running"]}
    ]
)

print("Running EC2 Instances")
print("---------------------")

found = False

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        found = True
        instance_id = instance["InstanceId"]
        instance_type = instance["InstanceType"]

        print(f"Instance ID: {instance_id}")
        print(f"Instance Type: {instance_type}")
        print("---------------------")

if not found:
    print("No running EC2 instances found.")




     



    






    
    








