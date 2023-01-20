#!/usr/bin/python
import boto3
import os
import json
import xmltodict
from datetime import datetime
import time

dynamodb = boto3.client('dynamodb',region_name=os.environ['AWS_REGION'])
cognito_id = os.environ["CognitoID"]
calling_domain = os.environ["CallingDomain"]
resource = os.environ["DomainName"]
outputfile = os.environ['EXECUTION_ID']
port = os.environ['PORT']
protocol = os.environ['PROTOCOL']
scan_type = os.environ['SCAN_TYPE']
# Getting the current date and time
dt = datetime.now()

# getting the timestamp
ts = time.mktime(dt.timetuple())
# Read file

filename="/openvas/results/" + outputfile  + ".xml"
with open(filename) as xml_file:
    file_content_data = xmltodict.parse(xml_file.read())
type_field = "VulnScan-" + scan_type
data=protocol + "://" + resource + ":" + port
# Put item into DynamoDB
file_content = file_content_data['report']['report']['host']
file_content_parse = file_content['detail']
for vuln_data in file_content_parse:
    if (vuln_data['value'] != "EXIT_NOTVULN") and (vuln_data['value'] != "Greenbone Community Feed"):
        try:
            dynamodb.put_item(
            TableName = "maxxscan-vuln",
            Item={
                "ID": {"S": cognito_id}, 
                "Data": {"S": str(vuln_data)}, 
                "CallingDomain": {"S": calling_domain}, 
                "Resource": {"S": data}, 
                "ScanType": {"S": "OPENVAS"}, 
                "CWE": {"S": str(vuln_data['source']['name'])},
                "Last_Detected": {"S": ts}
                })
        except Exception:
            continue
file_content = file_content_data['report']['report']['results']
file_content_parse = file_content['result']
for vuln_data in file_content_parse:
    try:
        dynamodb.put_item(
        TableName = "maxxscan-vuln",
        Item={
            "ID": {"S": cognito_id}, 
            "Data": {"S": str(vuln_data)}, 
            "CallingDomain": {"S": calling_domain}, 
            "Resource": {"S": data}, 
            "ScanType": {"S": "OPENVAS"}, 
            "CWE": {"S": str(vuln_data['nvt']['@oid'])},
            "Last_Detected": {"S": ts}
            })
    except Exception:
        continue

dynamodb.put_item(
    TableName = "maxxscan-intel",
    Item={
        "ID": {"S": cognito_id}, 
        "Data": {"S": data}, 
        "CallingDomain": {"S": calling_domain}, 
        "Resource": {"S": resource}, 
        "Type": {"S": type_field}
        })