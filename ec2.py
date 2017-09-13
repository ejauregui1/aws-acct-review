import datetime
import pprint
import boto3
import json

ec2 = boto3.client('ec2')

#Manual function to handle JSON Dump error with datetime
#def datetime_handler(x):
    #if isinstance(x, datetime.datetime):
        #return x.isoformat()
    #raise TypeError("Unknown type")

#Pull EC2 instances info as a dict variable
def info(d):
    for k , v in d.items():
        if isinstance(v,dict):
            info(v)
        else:
            pprint.pprint ("{0} : {1}".format(k, v))

#Get depth of dictionary
def dict_depth(d, depth=0):
    if not isinstance(d, dict) or not d:
        return depth
    return max(dict_depth(v, depth+1) for k, v in d.items())

instances = info(ec2.describe_instances())

#print (instances)
#instances = ec2.describe_instances()
#print (type(instances))

##Transferring dict into json form
#info = json.dumps(instances, default=datetime_handler)
#print (type(info))

#Displays instance information as JSON data
#pprint.pprint (instances)
#print (instances)
