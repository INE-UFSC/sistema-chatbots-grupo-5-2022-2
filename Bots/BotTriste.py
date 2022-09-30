from Bots.Bot import Bot

COMANDOS = {'Bom dia': 'Bom dia? Amigo, só dia, né, porque de bom não tem nada',
            'Qual o seu nome?': 'Eu sou o bot triste 😢', 'Quero um conselho': 'Desista', 'Adeus': 'Deus não existe'}


class BotTriste(Bot):
    def __init__(self):
        dict_comandos = dict()
        for i, comando in enumerate(COMANDOS):
            dict_comandos.update({str(i + 1): comando})
        super().__init__('Bot Triste', dict_comandos)

    def executa_comando(self, cmd):
        try:
            return COMANDOS[list(COMANDOS)[int(cmd) - 1]]
        except (ValueError, KeyError):
            return 'Eu nem tenho esse comando, tu acha que eu sou o que 😢'

    def boas_vindas(self):
        return 'Sai daqui mermão não te chamei 😢'

    def despedida(self):
        return COMANDOS['Adeus']
