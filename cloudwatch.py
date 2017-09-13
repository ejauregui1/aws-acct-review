from datetime import datetime, timedelta
import pprint
import boto3
import json

#S3 buckets & CloudWatch objects
s3 = boto3.resource('s3')
cloudwatch = boto3.client('cloudwatch')
asg = boto3.client('autoscaling')
cw = boto3.resource('cloudwatch')

print("S3 Buckets")
#print out bucket names
for bucket in s3.buckets.all():
  print (bucket.name)
print (" _____________________________________________________ ")

#List dashboards
dash1 = cloudwatch.list_dashboards()
print ("CloudWatch Dashboards:")
pprint.pprint(dash1)
print (" _____________________________________________________ ")

print("Cloudwatch List Metrics")
#List EC2 Metrics
dash2 = cloudwatch.list_metrics(
    Namespace='AWS/EC2'
)
pprint.pprint(dash2)
print (" _____________________________________________________ ")

print("Coudwatch Resources")
metric = cw.metrics.filter(
    Namespace='AWS/EC2'
)
pprint.pprint (metric)
print (" _____________________________________________________ ")

print ("Autoscaling Groups")
#ASG Information
groups = asg.describe_auto_scaling_groups()
pprint.pprint (groups)
print (" _____________________________________________________ ")

print ("Autoscaling Group Instances")
instances = asg.describe_auto_scaling_instances()
pprint.pprint (instances)
print (" _____________________________________________________ ")

print ("Autoscaling Metric Collection Types")
asgmetrics = asg.describe_metric_collection_types()
pprint.pprint (asgmetrics)
print (" _____________________________________________________ ")
