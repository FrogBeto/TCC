import requests
import json

class ListaDeRepositorios():
    def __init__(self, usuario):
        self._usuario = usuario
        self._valor = 0

    def requisicao_api(self):
        resposta = requests.get(
            #f'https://api.github.com/users/{self._usuario}/repos')
            f'https://api.github.com/repos/{self._usuario}/contributors?page={self._valor}')

        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def imprime_repositorios(self):
        #f = open("logins.txt", "x")
        dados_api = self.requisicao_api()

        if type(dados_api) is not int:
            with open("logins.txt", "w") as f:
                for j in range(14):
                    self._valor = j + 1
                    dados_api = self.requisicao_api()
                    for i in range(len(dados_api)):
                        f.write(dados_api[i]['login'] + " " + str(dados_api[i]['contributions']) + "\n")

            # open and read the file after the overwriting:
            with open("logins.txt") as f:
                print(f.read())

            #for i in range(len(dados_api)):
             #   print(dados_api[i]['login'])

        #._valor = 14
        #dados_api = self.requisicao_api()
        #if type(dados_api) is not int:
            #for i in range(len(dados_api)):
                #print(dados_api[i]['login'])

        else:
            print(dados_api)


repositorios = ListaDeRepositorios('arendst/Tasmota')
repositorios.imprime_repositorios()