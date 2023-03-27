import json
import boto3
import datetime

s3_client = boto3.resource('s3')

def lambda_handler(event, context):
    jsonObj = []
    for item in event["Items"]:
        obj = s3_client.Object(event["BatchInput"]["bucket"],
                                    item["Key"])
        data = obj.get()['Body'].read().decode('utf-8')
        json_data = json.loads(data)
        process_logs(json_data)
        
        jsonObj.append(process_logs(json_data))
    
    return {
        'Items': jsonObj
    }

def process_logs(obj):
    newObj = {}
    
    newObj["apiKey"] = obj["apiKey"]
    newObj["ip"] = obj["ip"]
    newObj["status"] = obj["status"]
    newObj["latency"] = obj["integrations"]["latency"].replace("-", "0")
    newObj["time"] = convertDate(obj["requestTime"])
    newObj["account"] = obj["account"]
    newObj["path"] = obj["resourcePath"]
    newObj["size"] = obj["responseLength"]
    newObj["method"] = obj["httpMethod"]
    newObj["reqId"] = obj["requestId"]
    
    return newObj
    
def convertDate(date):
    return str(datetime.datetime.strptime(date.split(" ")[0], '%d/%b/%Y:%H:%M:%S'))
