# Consumir APIs com Python - Converter Moedas - Finalização do Projeto https://www.youtube.com/watch?v=XhRYYrJZ-_E

import requests

def pegar_cotacao_moeda(moeda_origem, moeda_destino):
    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
    requisicao = requests.get(link)

    cotacao = requisicao.json()[f"{moeda_origem}{moeda_destino}"]["bid"]
    return cotacao

# 200 - requisição funcionou
