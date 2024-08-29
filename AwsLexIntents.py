import json
import datetime
import time
import re
from whois import whois
from datetime import datetime


def lambda_handler(event, context):
    intent = event['sessionState']['intent']['name']
    slots = event['sessionState']['intent']['slots']

    if event['invocationSource'] == 'FulfillmentCodeHook':
        #celular = slots['celular']['value']['originalValue']
        # Acessando o valor de 'originalValue' do campo 'URL'
        URL = slots['URL']['value']['originalValue']
        # Função para isolar os valores de 'originalValue'
        resultado_whois = whois.whois(URL)
        #
        dominio = resultado_whois.get("domain_name", "Informação não disponível")
        nome = resultado_whois.get("registrant_name", "Informação não disponível")
        pessoa = resultado_whois.get("person", "Informação não disponível")
        nome = resultado_whois.get("registrant_name", "Informação não disponível")
        cpf = resultado_whois.get("registrant_id", "Informação não disponível")
        email = resultado_whois.get("email", "Informação não disponível")
        pais = resultado_whois.get("country", "Informação não disponível")
        data = resultado_whois.get("creation_date", "Informação não disponível")
        realdata = data.strftime('%Y-%m-%d %H:%M:%S')
    
        
        
        
        response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    'name': intent,
                    'slots': slots,
                    'state': 'Fulfilled'

                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": f"Dominio: {dominio}  Nome: {nome} Pessoa: {pessoa}  CPF: {cpf}  Email: {email}  Pais: {pais}  Data de criação do site: {data} "
                }
            ]
        }

        return response


