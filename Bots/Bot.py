from abc import ABC, abstractmethod


class Bot(ABC):
    def __init__(self, nome, comandos):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    def mostra_comandos(self):
        texto = 'Digite o comando desejado (ou -1 fechar o programa sair): '
        for key in self.__comandos:
            texto += f'\n{key} - {self.__comandos[key]}'
        return texto

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass

    @abstractmethod
    def despedida(self):
        pass
