from Bots.Bot import Bot
from Bots.BotTriste import BotTriste
from Bots.BotZangado import BotZangado
from SistemaChatBot.SistemaChatBot import SistemaChatBot

sistema = SistemaChatBot("Grupo 5", BotTriste(), BotZangado())
sistema.inicio()
