# https://docs.aws.amazon.com/sdkref/latest/guide/common-runtime.html

import boto3

# Create EC2 client object
ec2 = boto3.client("ec2")

# Retrieve information about instances
response = ec2.describe_instances()

# Get the list of instances
instances = response["Reservations"][0]["Instances"]

# Loop over each instance
for instance in instances:
    # Print instance ID
    print(instance["InstanceId"])


# Create S3 bucket object
s3 = boto3.client("s3")

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
