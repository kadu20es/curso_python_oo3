import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
# print(response)
if response.status_code == 200:
    print('Requisição atendida com sucesso')
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company'] # cria um item para cada restaurante (company)
        if nome_do_restaurante not in dados_restaurante: 
            dados_restaurante[nome_do_restaurante] = [] # insere restaurante se ele não existir na lista
        
        # na lista do restaurante, cria dicionário por item daquele restaurante
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "preco": item['price'],
            "descricao": item['description']
        })
else:
    print(f'O erro foi {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    # cria um arquivo - 'w' = write
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)