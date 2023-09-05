import discord

class BotDiscord(discord.Client):
    def __init__(self,jstore):
        self.jstore=jstore
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        super().__init__(intents=self.intents)
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author.name == "jabl3s":
            self.jstore.setDiscord(message.content)
        else:
            return

#if message.content == 'ping':
#    await message.channel.send('pong')