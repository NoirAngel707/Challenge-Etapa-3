import whois
from datetime import datetime
import phonenumbers
from phonenumbers import geocoder, carrier
import difflib
import re

# Lista de domínios conhecidos
DOMINIOS_CONHECIDOS = [
    "google.com",
    "facebook.com",
    "twitter.com",
    "instagram.com",
    "amazon.com",
    "netflix.com",
    # Adicione mais domínios conhecidos conforme necessário
]

def formatar_data(data_criacao):
    if isinstance(data_criacao, list):
        data_criacao = data_criacao[0]  # Pega a primeira data da lista, se for uma lista
    if isinstance(data_criacao, datetime):
        return data_criacao.strftime('%Y-%m-%d %H:%M:%S')
    return "Data não disponível"

def calcular_dias(data_criacao):
    if isinstance(data_criacao, list):
        data_criacao = data_criacao[0]
    if isinstance(data_criacao, datetime):
        dias_passados = (datetime.now() - data_criacao).days
        return dias_passados
    return None

def analisar_telefone(telefone):
    try:
        # Remove espaços, parênteses e hífens
        telefone = re.sub(r"[^\d+]", "", telefone)

        # Adiciona o código do país se não estiver presente
        if not telefone.startswith("+"):
            telefone = "+55" + telefone
        
        numero = phonenumbers.parse(telefone, "BR")  # Especifica que é um número brasileiro
        ddd = str(numero.national_number)[:2]  # Extrai os dois primeiros dígitos como DDD
        pais = geocoder.country_name_for_number(numero, "pt")
        return ddd, pais
    except phonenumbers.NumberParseException as e:
        return None, None

def verificar_sinal_scam(URL, data_criacao, telefone):
    # Verifica se o número é de fora do Brasil
    ddd, pais = analisar_telefone(telefone)
    if pais != "Brasil":
        return "O número de telefone é internacional, o que pode ser um sinal de alerta."

    # Verifica a idade do domínio e cria um alerta baseado no tempo de criação
    dias_passados = calcular_dias(data_criacao)
    alerta_idade = ""
    if dias_passados is not None:
        if dias_passados < 30:
            alerta_idade = "O site foi criado há menos de 30 dias. Isso pode ser um sinal de alerta, pois sites muito novos podem ser arriscados."
        elif dias_passados < 90:
            alerta_idade = "O site foi criado há menos de 90 dias. Este é um período crítico para novos sites e pode indicar algum risco."
        elif dias_passados < 180:
            alerta_idade = "O site foi criado há menos de 180 dias. Embora não seja tão novo, ainda é relativamente recente."
        else:
            alerta_idade = "O site foi criado há mais de 180 dias. Isso sugere que o site tem um histórico mais longo e pode ser mais confiável."

    # Verifica se o nome do domínio é semelhante a domínios conhecidos
    dominio = URL.split('//')[-1].split('/')[0]  # Remove protocolo e caminhos
    dominio = dominio.lower()
    for conhecido in DOMINIOS_CONHECIDOS:
        similaridade = difflib.SequenceMatcher(None, dominio, conhecido).ratio()
        if similaridade > 0.7:  # Ajuste a similaridade conforme necessário
            return f"O nome do domínio é semelhante a um domínio conhecido: {conhecido}."

    return alerta_idade if alerta_idade else "Nenhum sinal claro de scam detectado."

def consulta_whois(URL, telefone):
    try:
        # Realiza a consulta WHOIS
        resultado = whois.whois(URL)
        
        # Extrai informações específicas para a resposta
        dominio = resultado.get("domain_name", "Informação não disponível")
        email = resultado.get("email", "Informação não disponível")
        data_criacao = resultado.get("creation_date", "Informação não disponível")
        
        # Formata a data de criação
        data_formatada = formatar_data(data_criacao)
        dias_passados = calcular_dias(resultado.get("creation_date"))

        # Analisa o telefone
        ddd, pais = analisar_telefone(telefone)

        # Verifica sinais de scam
        alerta_scam = verificar_sinal_scam(URL, resultado.get("creation_date"), telefone)

        # Formata a resposta de forma amigável
        response_text = (
            f"Informações sobre o domínio {URL}:\n"
            f"Telefone: {telefone}\n"
            f"DDD: {ddd if ddd else 'Informação não disponível'}\n"
            f"País: {pais if pais else 'Informação não disponível'}\n"
            f"Domínio: {dominio}\n"
            f"Email de contato: {email}\n"
            f"Data de criação: {data_formatada}\n"
        )
        
        # Adiciona condição baseada nos dias passados
        if dias_passados is not None:
            response_text += f"Este site foi criado há {dias_passados} dias.\n"
            response_text += alerta_scam
        
        else:
            response_text += "Não foi possível calcular a data de criação do site."
        
        print(response_text)
    
    except Exception as e:
        print(f"Erro ao consultar o domínio: {str(e)}")

# Solicita as entradas do usuário
telefone = input("Digite o número de telefone: ")
URL = input("Digite o link do site: ")

# Teste com o domínio e telefone fornecidos
consulta_whois(URL, telefone)
