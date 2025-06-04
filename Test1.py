import requests
import json

class ListaDeRepositorios():
    def __init__(self, usuario):
        self._usuario = usuario
        self._valor = 13

    def requisicao_api(self):
        resposta = requests.get(
            #f'https://api.github.com/users/{self._usuario}/repos')
            f'https://api.github.com/repos/{self._usuario}/contributors?page={self._valor}')

        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def imprime_repositorios(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['login'])

        #._valor = 14
        #dados_api = self.requisicao_api()
        #if type(dados_api) is not int:
            #for i in range(len(dados_api)):
                #print(dados_api[i]['login'])

        else:
            print(dados_api)


repositorios = ListaDeRepositorios('arendst/Tasmota')
repositorios.imprime_repositorios()