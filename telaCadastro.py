import json
import urllib.request

url_produtos = "http://localhost:3000/produtos"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def abrir():
    print("###########################")
    print("### CADASTRO DE PRODUTO ###")
    print("###########################")
    nome = input("Nome: \n")
    descricao = input("Descrição: \n")
    data_cadastro = input("Data Cadastro: \n")
    categoria = input("Categoria: \n")
    quantidade = input("Quantidade: \n")
    preco = input("Preço: \n")

    dados = {
        "nome": nome,
        "descricao": descricao,
        "quantidade": quantidade,
        "preco": preco,
        "categoria": categoria,
        "data_cadastro": data_cadastro
    }
    
    req = urllib.request.Request(
        url_produtos, 
        data = json.dumps(dados).encode('utf8'), 
        headers = headers,
        method = 'POST')
    
    resposta = urllib.request.urlopen(req)
    resposta_json = json.loads(resposta.read().decode('utf-8'))
    print(f"Produto cadastrado com sucesso, código: {resposta_json['id']}")
