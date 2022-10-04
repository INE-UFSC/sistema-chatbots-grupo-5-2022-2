from Bots.Bot import Bot
from Bots.BotTriste import BotTriste
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotZangado4 import BotZangado4
from Bots.BotTriste4 import BotTriste4
from Bots.BotFeliz4 import BotFeliz4
from SistemaChatBot.SistemaChatBot import SistemaChatBot

sistema = SistemaChatBot("Grupo 5", BotTriste(), BotZangado(), BotFeliz(), BotZangado4("Bot Zangado 4"), BotTriste4("Bot Triste 4"), BotFeliz4("Bot Feliz 4"))
sistema.inicio()
