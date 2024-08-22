import json
import datetime
import time
import whois
from datetime import datetime

def lambda_handler(event, context):
    
    intent = event['sessionState']['intent']['name']
    slots = event['sessionState']['intent']['slots']
    
    if event['invocationSource'] == 'FulfillmentCodeHook':
        celular = slots['celular']['value']['originalValue']
        # Acessando o valor de 'originalValue' do campo 'URL'
        URL = slots['URL']['value']['originalValue']
        # Função para isolar os valores de 'originalValue'
        resultado = whois.whois(URL)
        response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                'name':intent,
                'slots': slots,
                'state':'Fulfilled'
                
                }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": f"{resultado}"
            }
        ]
    }
            
        return response
        
        
        
