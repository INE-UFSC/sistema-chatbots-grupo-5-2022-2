from Bot import Bot

Comandos = {'Bom dia':'Que bom dia oque nem falei com você', 'Qual seu nome': 'Sou o bot zangado e poderia ir embora!', 'Quero um conselho': 
            'Não incomode as pessoas!', 'Adeus': 'Se nem dei bom dia você acha que vou me despedir?'}

class BotZangado(Bot):
    def __init__(self):
        dict_comandos = dict()
        for i, comando in enumerate(Comandos):
            dict_comandos.update({str(i + 1): comando})
        super().__init__('Bot Zangado', dict_comandos)

    def executa_comando(self,cmd):
        try:
            return Comandos[list(Comandos)[int(cmd) - 1]]
        except(ValueError, KeyError):
            return 'Oque você tá falando? para de incomodar'

    def despedida(self):
        return 'Ainda bem que vai embora não aguentava mais'
    
    def boas_vindas(self):
        return 'Oque você está fazendo aqui vai embora?
        
