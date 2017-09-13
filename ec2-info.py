import pprint
import boto3
import jmespath

ec2 = boto3.client('ec2')

#Pull EC2 instances info as a dict variable
ec2_res = ec2.describe_instances()

instances = jmespath.search("Reservations[].Instances[].NetworkInterfaces[].PrivateIpAddresses[].Association.PublicIp", ec2_res)
print(instances)
