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
    else:s))
    #print(resultado_whois)

  
        formatted_dates = [datetimes.strftime('%Y-%m-%d %H:%M:%S')] if isinstance(datetimes, datetime) else []

    if formatted_dates:
        data = (formatted_dates[0])
        print("DATA DE CRIAÇÃO DO SITE: " + data)


    else:
        print("DATA DE CRIAÇÃO DO SITE: N/A")
  
    # No Código abaixo é feita uma tentativa de forjar uma requisição para o cadastropre enviando como payload o CPF anteriormente coletado.
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0'
        'Content-Type = application/x-www-form-urlencoded'

    }

    payload = {
        "cpf":f"{cpf}"
         # Corrigido a chave 'doc' e o valor cpf
    }

    url = 'https://cadastropre.com.br'  # Certifique-se de que a URL é correta

    try:
        with requests.Session() as session:
            response = session.post(url, headers=headers, data=payload)
            if response.status_code == 200:
                print(f"Dados enviados com sucesso. Status Code: {response.status_code}")
               # print("Resposta do servidor:", response.text)
            else:
                print(f"Erro ao enviar dados. Status Code: {response.status_code}")
               #print("Resposta do servidor:", response.text)
    except Exception as e:
        print(f"Erro ao enviar dados: {e}")

else:
    print("Não foi possível obter informações sobre o domínio.")


