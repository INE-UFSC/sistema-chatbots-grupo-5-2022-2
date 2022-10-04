#Grupo 4

from Bots.Bot import Bot
import random

COMANDOS={"Bom dia": "Que lindo dia para falar com uma pessoa legal!",
                                   "Qual é o seu nome?": f"Meu nome é Bot Feliz e mal te conheci e já te amooo!",
                                   "Conselho": ["Ajeite a postura.",
                                                "Ligue para a sua mãe.",
                                                "Diga saude quando alguem espirrar.",
                                                "Beba água."],
                                   "Adeus": "Auf wiedersehen! Até mais ver, sentirei saudades."}

class BotFeliz4(Bot):
    def __init__(self,nome):
        super().__init__(nome,
                         COMANDOS)
  
    def executa_comando(self, cmd):
        cmd = int(cmd)
        try:
            if cmd == 3:
                return COMANDOS[list(COMANDOS)[cmd - 1]][random.randint(0,3)]
            return COMANDOS[list(COMANDOS)[cmd - 1]]
        except ValueError as e:
            print(e)

    def apresentacao(self):
        return f"Me chamo {self.nome}, prazer em conhecer você!"

    def boas_vindas(self):
        return "Ainda bem que você me escolheu!"

    def despedida(self):
        return "Ahhh que pena, queria conversar mais contigo. Ate a proxima!"
