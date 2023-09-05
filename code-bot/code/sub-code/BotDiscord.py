import discord

class BotDiscord(discord.Client):
    def __init__(self,jstore):
        self.__jstore=jstore
        self__intents = discord.Intents.default()
        self__intents.message_content = True
        super().__init__(intents=self__intents)
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author.name == "jabl3s":
            self.__jstore.__setDiscord(message.content)
        else:
            return

#if message.content == 'ping':
#    await message.channel.send('pong')