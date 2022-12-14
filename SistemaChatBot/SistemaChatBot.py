from multiprocessing.sharedctypes import Value
from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,*lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        for bot in lista_bots:
            if not isinstance(bot, Bot): 
                raise ValueError # A lista possui um valor que não é um Bot
        self.__lista_bots=list(lista_bots)
        self.__bot = None
    
    def boas_vindas(self):
        print("> Sistema: Bem vindo ao sistema de bots do " + self.__empresa)

    def mostra_menu(self):
        ##mostra o menu de escolha de bots
        print("> Sistema: Digite -1 para sair do sistema")
        print("Os bots disponíveis são: ")
        for i, bot in enumerate(self.__lista_bots):
            print("   " + str(i) + " - " + bot.nome + ": " + bot.boas_vindas())
        print("")

    def escolhe_bot(self):
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 
        n_bots = len(self.__lista_bots)

        while True: # Pega a entrada até ser válida
            try:
                print("Digite o número do bot escolhido: ", end="")
                entrada = int(input())
                if not -1 <= entrada < n_bots: 
                    raise ValueError # Erro no valor de entrada
            except ValueError:
                print("Entrada inválida\n")
                continue
            break
        if entrada == -1:
            self.__bot = None
        else:
            self.__bot = self.__lista_bots[entrada]

    def mostra_comandos_bot(self):
        ##mostra os comandos disponíveis no bot escolhido
        print("\nDigite -1 para ir para a seleção de bots")
        print("Comandos do " + self.__bot.nome)
        print(self.__bot.mostra_comandos())
        print("")

    def le_envia_comando(self):
        ##faz a entrada de dados do usuário e executa o comando no bot ativo
        print("Digite o comando a ser executado: ")
        while True: # Pega a entrada até ser válida
            print("> Você diz: ", end="")
            entrada = input()
            if entrada not in self.__bot.comandos.keys() and entrada != "-1": 
                print("Comando inválido\n")
                continue # Comando não está na lista de comandos
            break
        if entrada == "-1": # Sai do loop de seleção de comandos
            return False

        print("> " + self.__bot.nome + " diz: " + self.__bot.executa_comando(entrada))
        return True # True para continuar no loop de comandos

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        self.boas_vindas()

        while True:
            ##mostra o menu ao usuário
            self.mostra_menu()
            ##escolha do bot  
            self.escolhe_bot()
            if self.__bot == None: break # Sai do sistema

            ##mostra mensagens de boas-vindas do bot escolhido
            print(self.__bot.boas_vindas())
            while True:
                ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
                self.mostra_comandos_bot()
                loop = self.le_envia_comando()
                if not loop:
                    print("> " + self.__bot.nome + ": " + self.__bot.despedida())
                    break # Sai do loop de comandos
