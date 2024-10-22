#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS
#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar
#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico
#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]
lista_produtos_maior30 = []
for dados_response in response:
    for y in dados_response['produtos']:
        if y['preço'] > 30:
            item_30 = {
                'nome' : y['nome'],
                'preço' : y['preço']
            }
            lista_produtos_maior30.append(item_30)
for itens in lista_produtos_maior30:
    print(f"Produto: {itens['nome']}, Preço: {itens['preço']}")
    print("-="*60)
"""
      
    Decidi utilizar essa solução que realiza iterações aninhadas para localizar as chaves nome e preço, retirando e colocando esses itens em uma nova lista de produtos denominada lista_produtos_maior30.
    Essa abordagem facilita a análise dos produtos que atendem ao critério de preço maior que 30 reais.
    Além disso, a iteração aninhada é essencial porque, se por algum motivo a chave produtos tiver que ser alterada ou se forem adicionadas mais chaves dentro da lista, mudando o índice de nome e preço,
    o algoritmo ainda será capaz de localizar esses valores corretamente.
    Essa escolha justifica o uso de iterações aninhadas, em vez de um acesso direto aos valores, tornando o código dinâmico. Embora isso aumente o custo da operação em termos de complexidade.
"""
#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra
responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}
produto_B = responsejson['produtos'][1]['preço']
print(f"{produto_B}")
"""
        Diferentemente do caso número 1, este JSON contém apenas uma loja, o que restringe o escopo e dá a entender que é uma requisição específica,
    com parâmetros bem definidos. Sendo assim, decidi realizar um acesso direto às chaves, sem desenvolver um algoritmo de busca, pois já conhecemos a estrutura e os parâmetros exatos do local.
        Dessa forma, poupamos processamento, uma vez que o uso de iterações ou algoritmos de busca não seria necessário em um cenário tão simples e controlado.
"""
#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra
lista = [5,8,3,0,8,1,9,10,20,30]
lista_ordenada = sorted(lista)
print(lista_ordenada)
"""
 Ainda pensando em custo de processamento, como lista contem apenas 10 itens, a criação de uma nova lista ordenada utilizando a função sorted()
foi a melhor opção, pois assim não perderemos a lista original.
"""
#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela
lista = ["   joao   ","   maria   ","  joana  "]
lista_SemEspacos = []
for palavra in lista:
    lista_SemEspacos.append(palavra.strip())
print(lista_SemEspacos)
#5-Retire o segundo item dessa lista e imprima ela:
lista = [1,2,3,4,5,6]
lista.pop(1)
print(lista)
#6-substitua todos os "joao" da lista por "maria"
lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]
print(lista)
for posicao, palavra in enumerate(lista):
    if palavra == "joao":
        lista[posicao]="maria"
print(lista)
        
    
#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra
x = 0
while x <=5:
    print(lista[x])
    x += 1
"""
O problema é bem simples, não requer muita complexidade. 
Como está expecificado para utilizar um while, segui as regras, mas seria melhor ainda com um for
"""
#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra
import requests
def buscar_Param_Json(url, *parametros_request):
    lista_respostas = list()
    for valoes_request in parametros_request:
        request_resposta = requests.get(url, params= valoes_request)
        resposta = request_resposta.json()
        lista_respostas.append(resposta)
    return lista_respostas
url = 'https://jsonplaceholder.typicode.com/todos'
parametro = {'completed': 'false'}
parametro2 = {'completed': 'true'}
tasks = buscar_Param_Json(url, parametro, parametro2)
print(f"A quantidade de tarefas completas: {len(tasks[1])}")
print(f"A quantidade de tarefas incompletas: {len(tasks[0])}")
"""
A criação do método buscar_Param_Json recebe como argumentos a URL da API (https://jsonplaceholder.typicode.com/users) e os parâmetros *parametros_request, que incluem os valores de completed como true e false. A utilização do operador * permite a inserção dinâmica de múltiplos parâmetros de requisição, o que oferece flexibilidade. Dessa forma, se for necessário adicionar mais parâmetros de pesquisa no futuro, isso pode ser feito facilmente.
Optei por essa abordagem porque, ao fazer duas requisições separadas e retornando apenas os dados solicitados, a utilização de memória fica otimizada, já que apenas os dados relevantes são manipulados. Além disso, esse método ajuda a evitar um possível vazamento de dados, uma vez que estamos controlando o que é retornado e processado.
"""
#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra
url = 'https://jsonplaceholder.typicode.com/users'
request_usuarios= requests.get(url)
usuarios = request_usuarios.json()
lista_dados= list()
for x in usuarios:
    dados = {
        'nome': x['name'],
        'username' : x['username'],
        'email' : x['email'],
        'rua' : x['address']['street'],
        'numero' : x['address']['suite']
    }
    lista_dados.append(dados)
for x in lista_dados:
    print(f"Nome: {x['nome']}, Username: {x['username']}, Email: {x['email']} , Rua: {x['rua']}, Número: {x['numero']}")
    print('-'*100)
"""
    Nesta tarefa, foi necessária a criação de um JSON para a obtenção de dados, 
    onde utilizei meus conhecimentos sobre dicionários e estrutura de dados em Python para extrair as informações corretas do JSON
      e criar uma lista contendo todos os usuários requisitados.
    Ao iterar sobre os dados retornados pela requisição, extraí as informações de interesse (nome, username, email, rua e número)
      e as organizei em um novo dicionário, que foi adicionado à lista. Isso permitiu um controle preciso dos dados retornados, facilitando a exibição das informações de forma clara e organizada.
"""
#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO
lista = [1,2,3,4,5]
lista.insert(0, 67)
lista.pop(0)
#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO
lista = [1,2,3,4,5]
lista.append(6)
lista.pop()
print(lista)
#DESAFIO!!
#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta
class Conta:
    contador_id = 1
    
    def __init__(self, nome, cpf):
        self.__id = Conta.contador_id
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = 0.0
        Conta.contador_id += 1
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, novo_saldo):
        self.__saldo = novo_saldo 
        
    def informacoes_conta(self):
        print(f"Nome:{self.get_nome()}, saldo R${self.get_saldo():.2f}")
class Operacoes:
    
    def __init__(self, conta):
        self.conta = conta
    def saque(self, quantidade_saque):
        self.quantidade_saque = quantidade_saque
        if quantidade_saque > self.conta.get_saldo():
            print("Saldo insulficiente para realizar o saque")
        elif quantidade_saque <= 0 :
            print("Saque inválido")
        else:
            saldoapossaque = float(self.conta.get_saldo() - quantidade_saque)
            self.conta.set_saldo(saldoapossaque)
            print(f"Saque realizado de R${self.quantidade_saque}, novo saldo R${self.conta.get_saldo():.2f}")
    def deposito(self, deposito):
        self.deposito = deposito
        if deposito > 0:
            saldodesposito = float(self.conta.get_saldo() + deposito)
            self.conta.set_saldo(saldodesposito)
            print(f"Deposito realizado de {self.deposito}, novo saldo R${self.conta.get_saldo():.2f}")
            
        else:
            print("Depósito inválido")
    
if __name__ == "__main__":
    
    conta = Conta("Gustavo Mascarenhas dos santos" , "1231233312")
    operacoes_conta = Operacoes(conta)
    
    operacoes_conta.deposito(1000000)  
        
    print("=-" * 30)
    operacoes_conta.saque(500) 
    
    print("=-" * 30)
    conta.informacoes_conta()
    conta2 = Conta("test2" , "123123331324232")
    operacoes_conta = Operacoes(conta2)
    
    operacoes_conta.deposito(1000000)  
        
    print("=-" * 30)
    operacoes_conta.saque(500) 
    
    print("=-" * 30)
    conta2.informacoes_conta()
