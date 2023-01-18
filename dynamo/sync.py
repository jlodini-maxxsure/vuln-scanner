#!/usr/bin/python
import boto3
import os

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
cognito_id = os.environ["CognitoID"]
calling_domain = os.environ["CallingDomain"]
resource = os.environ["DomainName"]
outputfile = os.environ['EXECUTION_ID']
resource_type = "VulnScan"
# Read file
filename="/openvas/results/" + outputfile  + ".xml"
with open(filename, 'r') as file:
    file_content = file.read()

# Put item into DynamoDB
dynamodb.put_item(
    Item={
        "ID": {"S": cognito_id}, 
        "Data": {"S": file_content}, 
        "CallingDomain": {"S": calling_domain}, 
        "Resource": {"S": resource}, 
        "Type": {"S": resource_type}
        })
