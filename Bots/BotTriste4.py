# Grupo 4

from Bots.Bot import Bot
import random

COMANDOS ={"Bom dia": "Oi.",
                                   "Qual é o seu nome?": f"Ah, é BOT Triste.",
                                   "Conselho": ["Nada está tão ruim que não possa piorar.",
                                                "É mais fácil lidar com a depressão estando bêbado.",
                                                "Apenas seja feliz.",
                                                "Here's a little song I wrote, you might want to sing it note for note: Don't worry."],
                                   "Adeus": "Não se vá..."}

class BotTriste4(Bot):
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
        return f"Me chamo {self.nome}."

    def boas_vindas(self):
        return "Qual o motivo para comemorar uma vinda?"

    def despedida(self):
        return "Sozinho denovo..."
