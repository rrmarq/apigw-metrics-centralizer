import json
import datetime

def lambda_handler(event, context):
    message = event['Records']
    
    cont = 1
    reason = "Segue abaixo execucoes no API Gateway no dia " + datetime.datetime.now().strftime("%d/%m/%Y") + ". \n" \
                "Para mais detalhes e custo acesso o Quicksight no endereco  " + event["URLQuickSight"] + " \n"
    while cont < len(message):
        m =  "A ApiKey {} teve {} execucoes na conta {} com total de {} bytes trafegados. \n"
        m = m.format(message[cont]['Data'][0]['VarCharValue'], 
                                message[cont]['Data'][2]['VarCharValue'], 
                                message[cont]['Data'][1]['VarCharValue'], 
                                message[cont]['Data'][5]['VarCharValue'])
        reason = reason + m
        cont = cont + 1

    print(reason)
    return {
        'statusCode': 200,
        'body': json.dumps(reason)
    }
