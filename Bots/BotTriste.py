from Bots.Bot import Bot

COMANDOS = {'Bom dia': 'Bom dia? Amigo, só dia, né, porque de bom não tem nada',
            'Qual o seu nome?': 'Eu sou o bot triste 😢', 'Quero um conselho': 'Desista'}


class BotTriste(Bot):
    def __init__(self):
        super().__init__('Bot Triste', COMANDOS)

    def executa_comando(self, cmd):
        try:
            return COMANDOS[list(COMANDOS)[int(cmd) - 1]]
        except (ValueError, KeyError):
            return 'Eu nem tenho esse comando, tu acha que eu sou o que 😢'

    def boas_vindas(self):
        return 'Sai daqui mermão não te chamei 😢'

    def despedida(self):
        return 'Deus não existe'
