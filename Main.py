from Bots.Bot import Bot
from Bots.BotTriste import BotTriste
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from SistemaChatBot.SistemaChatBot import SistemaChatBot

sistema = SistemaChatBot("Grupo 5", BotTriste(), BotZangado(), BotFeliz())
sistema.inicio()
