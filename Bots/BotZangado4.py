from sympy import O
#Grupo 4

from Bots.Bot import Bot
import random

COMANDOS={"Bom dia": "Vai se lascar, você me acordou!",
                                   "Qual é o seu nome?": f"Não sabe ler? Bot zangado, seu analfabeto.",
                                   "Conselho": ["Conselho? Me pague.",
                                                "Digite -1 para ver um comando legal.",
                                                "Nada vem de graça, nem o pão, nem a cachaça, e nem o conselho.",
                                                "Beba corote na promoção."],
                                   "Adeus": "Já vai tarde."}

class BotZangado4(Bot):
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
        return f"Quê? Conversar? Mas eu estava dormindo! Nome? {self.nome}"

    def boas_vindas(self):
        return "Diabo de conversa o quê, me deixa em paz."

    def despedida(self):
        return "Aleluia! Vou voltar a dormir."
