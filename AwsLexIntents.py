#aws lambda code for 
#How to Make a Chatbot Using Amazon Lex and AWS Lambda (Python) | Conversational AI Part 2
# https://youtu.be/W6T-RFei6SY
import json
import datetime
import time


def lambda_handler(event, context):
#Função que recebe o nome da Intent e o tipo de evento
    intent = event['sessionState']['intent']['name']
#Linha que recebe o nome dos slots e os valores do mesmo.
    slots = event['sessionState']['intent']['slots']
#Essa condição ela é atendida sempre que um evento de FulfillmentCodeHook for recebida, no Amazon Lex definimos que após todos os slots forem preenchidos um Evento de Fulfillment é enviado
    if event['invocationSource'] == 'FulfillmentCodeHook':
     
   
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
#Retornando o payload dos slots
                "content": f"{slots}"
            }
        ]
    }       
        return response
