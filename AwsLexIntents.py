import json
import datetime
import time
from whois import whois
from datetime import datetime

def lambda_handler(event, context):
    
    
    intent = event['sessionState']['intent']['name']
    slots = event['sessionState']['intent']['slots']
    
    
    if event['invocationSource'] == 'FulfillmentCodeHook':
        celular = slots['celular']['value']['originalValue']
        # Acessando o valor de 'originalValue' do campo 'URL'
        URL = slots['URL']['value']['originalValue']
        # Função para isolar os valores de 'originalValue'
        resultado_whois = whois.whois(URL) 
        dominio = resultado_whois.get("domain_name", "N/A")
        nome = resultado_whois.get("registrant_name", "N/A")
        pessoa = resultado_whois.get("person", "N/A")
        nome = resultado_whois.get("registrant_name", "N/A")
        cpf = resultado_whois.get("registrant_id", "N/A")
        email = resultado_whois.get("email", "N/A")
        pais = resultado_whois.get("country", "N/A")
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
                "content": f"Dominio: {dominio}  Nome: {nome}  Pessoa: {pessoa}  CPF: {cpf}   email: {email}  nacionalidade: {pais}"
            }
        ]
    }
            
        return response
        
        
        
