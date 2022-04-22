from asyncio import constants
from email.errors import MessageError
import discord
from constants import BotMessages

class Bot(object):

    async def register(self, message):
        
        boasVindas_embed_msg = discord.Embed(title = BotMessages.GREETINGS_TEXT_TITLE, description = BotMessages.GREETINGS_TEXT_DESCRIPTION, colour = BotMessages.GREETINGS_TEXT_COLOUR)
        boasVindas_embed_msg.set_image(url = "https://static.wikia.nocookie.net/leagueoflegends/images/e/eb/Trundle_OriginalSkin_old.jpg/revision/latest?cb=20201226020654")
        await message.author.send(embed = boasVindas_embed_msg)

        registro_embed_msg = discord.Embed(title = BotMessages.REGISTER_TEXT_TITLE, description = BotMessages.REGISTER_TEXT_DESCRIPTION, colour = BotMessages.REGISTER_TEXT_COLOUR)
        await message.author.send(embed = registro_embed_msg)
 