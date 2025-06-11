import requests
import json

token = ""
headers = {
    "Authorization": "token {}".format(token)
}

class ListaDeRepositorios():
    def __init__(self, usuario):
        self._usuario = usuario
        self._valor = 0

    def requisicao_api(self):
        resposta = requests.get(
            f'https://api.github.com/repos/{self._usuario}/contributors?per_page=100&page={self._valor}', headers=headers)

        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def imprime_repositorios(self):
        #f = open("usuarios2.txt", "x")
        dados_api = self.requisicao_api()

        if type(dados_api) is not int:
            with open("usuarios2.txt", "w") as f:
                for j in range(1):
                    self._valor = j + 1
                    dados_api = self.requisicao_api()
                    for i in range(len(dados_api)):
                        f.write(dados_api[i]['login'] + ", " + str(dados_api[i]['contributions']) + "\n")

                    if not dados_api:
                        print("Nenhum login foi encontrado na lista!")
                        break

            # open and read the file after the overwriting:
            with open("usuarios2.txt") as f:
                print(f.read())

        else:
            print(dados_api)

#Teste para um repositório
#repositorios = ListaDeRepositorios('arendst/Tasmota')
#repositorios.imprime_repositorios()

#URL base com o repositorio, requisição, número por páginas e número da página
#https://api.github.com/repos/arendst/Tasmota/contributors?per_page=100&page=1

#Lê o arquivo de projetos e faz a coleta de dados
with open("projetos.txt") as f:
  for x in f:
    print(x.strip())
    repositorios = ListaDeRepositorios(x)
    repositorios.imprime_repositorios()

#Teste de limite de requisições e limite de requisições autenticadas (com headers), além de entender melhor a estrutura da API
#data = requests.get(f' https://api.github.com/rate_limit').json()
#print(data['resources']['core']['remaining'])

#Teste de for
#for i in range(10):
 #   for j in range(6):
  #      if j > 4:
   #         print("Teste")
    #        break