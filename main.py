import pandas as pd
import requests

#Token de identificação da requisição - aumenta o limite por hora
token = ""
headers = {
    "Authorization": "token {}".format(token)
}

#Leitura do csv com os projetos e criação dos vetores para armazenar os donos dos repositórios e os seus projetos
df = pd.read_csv('projetos.csv')
donos = []
projetos = []

#Criação da lista de donos e projetos
for x in df['Dono']:
    donos.append(x)
for x in df['Projeto']:
    projetos.append(x)

#Classe responsavel por receber o nome do dono e do projeto e fazer a requisição para a api do GitHub
class Busca:
    #Atribuindo os valores
    def __init__(self, dono, projeto):
        self.dono = dono
        self.projeto = projeto
        self.valor = 1

    #responsavel pela requisição, retornando o valor ou o código de erro, caso tenha
    def requisicao(self):
        reposta = requests.get(
            f'https://api.github.com/users/{self.dono}',
            headers=headers
        )

        if reposta.status_code == 200:
            return reposta.json()
        else:
            return reposta.status_code

    #Pede uma requisição e gravas os contribuidores, quantidade de contribuições e projeto de origem num cvs
    def gravacao(self):
        dados = self.requisicao()

        if type(dados) is not int:
            with open("donos.csv", "a") as f:
                f.write(
                    self.dono + "," + dados['location'] + "," + str(dados['public_repos']) + "," + str(dados['followers']) + "," +
                    str(dados['following']) + "," + dados['created_at'] + "," + dados['updated_at'] + "\n")

                #while dados:
                    #for i in range(len(dados)):
                        #f.write(dados[i]['login'] + "," + str(dados[i]['contributions']) + "," + self.projeto + "\n")

                    #Atualiza a página e refaz a requisição
                    #self.valor += 1
                    #dados = self.requisicao()


#Responsavel por percorrer o vetor de donos e seus projetos, fazendo uma requisição a cada novo projeto
for x in range(len(donos)):
    repositorios = Busca(donos[x], projetos[x])
    repositorios.gravacao()


#Links já utilizados:
#https://api.github.com/repos/{self.dono}/{self.projeto}/contributors?per_page=100&page={self.valor}
#--> Gerou usuarios.csv
#https://api.github.com/repos/{self.dono}/{self.projeto}
#--> Gerou repositorios.csv
#https://api.github.com/users/{self.dono}
#--> Gerou donos.csv