#!/usr/bin/python
import boto3
import os

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('maxxscan-intel')
cognito_id = os.environ["CognitoID"]
calling_domain = os.environ["CallingDomain"]
resource = os.environ["DomainName"]
outputfile = os.environ['EXECUTION_ID']
resource_type = "VulnScan"
# Read file
with open('file.txt', 'r') as file:
    file_content = file.read()

# Put item into DynamoDB
table.put_item(Item={'ID: cognito_id, 'Data': file_content, 'CallingDomain': calling_domain, 'Resource': resource, 'Type': resource_type})
