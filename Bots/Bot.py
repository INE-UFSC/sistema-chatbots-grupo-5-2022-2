from abc import ABC, abstractmethod


class Bot(ABC):
    def __init__(self, nome, comandos):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self) -> str:
        return self.nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def mostra_comandos(self):
        texto = 'Digite o comando desejado (ou -1 fechar o programa sair): '
        for i, comando in enumerate(self.__comandos):
            texto += f'\n{i + 1} - {comando}'
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
