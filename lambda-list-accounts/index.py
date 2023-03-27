import json
import boto3

organizations = boto3.client('organizations')

def lambda_handler(event, context):
    
    objOrgs = organizations.list_accounts()

    objInpupt = []
    for account in objOrgs['Accounts']:
        if account['Id'] != event['central_account']:
            objTemp = {
                'account': account['Id'],
                'data_exec': event['data_exec'],
                'role-to-assume': 'arn:aws:iam::' + account['Id'] + ':role/logs-local-us-east-1',
                'bucket_central': 'logs-centralizer-' + event['central_account']
            }
            objInpupt.append(objTemp)

    return objInpupt
