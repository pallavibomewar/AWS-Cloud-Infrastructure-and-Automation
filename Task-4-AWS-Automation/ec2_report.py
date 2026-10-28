
import boto3

ec2 = boto3.client("ec2")

response = ec2.describe_instances(
    Filters=[
        {"Name": "instance-state-name", "Values": ["running"]},
        {"Name": "tag:Environment", "Values": ["dev"]}
    ]
)

# Example rates only, not live AWS pricing
hourly_rates = {
    "t2.micro": 0.0116,
    "t3.micro": 0.0104,
    "t3.small": 0.0208
}

total_monthly_cost = 0
found = False

print("Development EC2 Instance Report")
print("--------------------------------")

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        found = True
        instance_id = instance["InstanceId"]
        instance_type = instance["InstanceType"]

        print(f"Instance ID: {instance_id}")
        print(f"Instance Type: {instance_type}")

        hourly_cost = hourly_rates.get(instance_type)

        if hourly_cost is not None:
            monthly_cost = hourly_cost * 730
            total_monthly_cost += monthly_cost
            print(f"Estimated Monthly Cost: ${monthly_cost:.2f}")
        else:
            print("Estimated Monthly Cost: Rate unavailable")

        print("--------------------------------")

if not found:
    print("No running development EC2 instances found.")

print(f"Total Estimated Monthly Cost: ${total_monthly_cost:.2f}")





     



    






    
    








