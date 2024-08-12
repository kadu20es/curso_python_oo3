from fastapi import FastAPI, Query
import requests

app = FastAPI()


@app.get('/api/hello')
def hello_word():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação.
    '''
    return {'Hello':'world'}

@app.get('/api/restaurante/')
def obter_restaurante(restaurante: str = Query(None)):
    '''
    Endpoint que exibe os cardápios dos restaurantes.
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json} # retorna todos os dados
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "preco": item['price'],
                    "descricao": item['description']
                })
            return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
        else:
            return {'Erro':f'{response.status_code} - {response.text}'}