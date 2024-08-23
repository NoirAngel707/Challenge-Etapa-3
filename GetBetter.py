import requests
import whois
from datetime import datetime

def consulta_whois(dominio):
    try:
        # Consulta o WHOIS para o domínio fornecido
        resultado = whois.whois(dominio)
        # Armazena o resultado em uma variável
        return resultado
    except Exception as e:
        print(f"Erro ao consultar o domínio: {e}")
        return None

# Recebe o domínio como entrada
dominio = input("Digite o domínio para consultar WHOIS: ")
# Faz a consulta e armazena o resultado
resultado_whois = consulta_whois(dominio)

if resultado_whois:
    print("Informações sobre o Site:")
    dominio = resultado_whois.get("domain_name", "N/A")
    print("Dominio: " + str(dominio))
    nome = resultado_whois.get("registrant_name", "N/A")
    print(f"Nome/Empresa: {nome}")
    pessoa = resultado_whois.get("person", "N/A")
    print("Nome da Pessoa que criou o site: " + str(pessoa))
    nome = resultado_whois.get("registrant_name", "N/A")
    cpf = resultado_whois.get("registrant_id", "N/A")
    print("CPF/CNPJ: " + str(cpf))
    email = resultado_whois.get("email", "N/A")
    print("EMAIL: " + str(email))
    pais = resultado_whois.get("country", "N/A")
    print("NACIONALIDADE: " + str(pai  # Trata a criação de data que pode ser uma lista
    datetimes = resultado_whois.get("creation_date", [])
    if isinstance(datetimes, list):
        formatted_dates = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in datetimes if isinstance(dt, datetime)]
          else:

  
        formatted_dates = [datetimes.strftime('%Y-%m-%d %H:%M:%S')] if isinstance(datetimes, datetime) else []

    if formatted_dates:
        data = (formatted_dates[0])
        print("DATA DE CRIAÇÃO DO SITE: " + data)


    else:
        print("DATA DE CRIAÇÃO DO SITE: N/A")
  
