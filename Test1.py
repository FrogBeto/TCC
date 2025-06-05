import requests
import json

class ListaDeRepositorios():
    def __init__(self, usuario):
        self._usuario = usuario
        self._valor = 0

    def requisicao_api(self):
        resposta = requests.get(
            f'https://api.github.com/repos/{self._usuario}/contributors?page={self._valor}')

        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def imprime_repositorios(self):
        #f = open("usuarios.txt", "x")
        dados_api = self.requisicao_api()

        if type(dados_api) is not int:
            with open("usuarios.txt", "w") as f:
                for j in range(15):
                    self._valor = j + 1
                    dados_api = self.requisicao_api()
                    for i in range(len(dados_api)):
                        f.write(dados_api[i]['login'] + " " + str(dados_api[i]['contributions']) + "\n")

                    if len(dados_api) == 0:
                        print("Nenhum login foi encontrado na lista!")

            # open and read the file after the overwriting:
            with open("usuarios.txt") as f:
                print(f.read())

        else:
            print(dados_api)


#repositorios = ListaDeRepositorios('arendst/Tasmota')
#repositorios.imprime_repositorios()
#https://api.github.com/repos/arendst/Tasmota/contributors?page=1

#with open("projetos.csv") as f:
 # for x in f:
  #  print(x)