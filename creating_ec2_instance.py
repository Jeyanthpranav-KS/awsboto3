#creating an ec2 instance using boto3

import boto3

def creating_ec2_instance():
    try:
        print("Creating an ec2 instance using boto3")
        instance = boto3.client("ec2")
        instance.run_instances(
        ImageId='ami-0c2b8ca1dad447f8a',
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ec2"

        )

    except Exception as e:
        print(e)

def terminating_ec2_instance():
    try:
        print("Terminating an ec2 instance using boto3")
        instance = boto3.client("ec2")
        instance.terminate_instances(InstanceIds=["i-07cec914d879f583b"])

    except Exception as e:
        print(e)

creating_ec2_instance()
terminating_ec2_instance()

