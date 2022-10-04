from Bots.Bot import Bot

COMANDOS = {'Bom dia': 'Que bom dia oque nem falei com você', 'Qual seu nome': 'Sou o bot zangado e poderia ir embora!',
            'Quero um conselho':
                'Não incomode as pessoas!'}


class BotZangado(Bot):
    def __init__(self):
        super().__init__('Bot Zangado', COMANDOS)

    def executa_comando(self, cmd):
        try:
            return COMANDOS[list(COMANDOS)[int(cmd) - 1]]
        except(ValueError, KeyError):
            return 'Oque você tá falando? para de incomodar'

    def despedida(self):
        return 'Ainda bem que vai embora não aguentava mais'

    def boas_vindas(self):
        return 'Oque você está fazendo aqui vai embora?'
