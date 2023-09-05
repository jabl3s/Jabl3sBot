import discord

class BotDiscord(discord.Client):
    def __init__(self,jstore):
        self.jstore=jstore
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author.name == "jabl3s":
            self.jstore.discord.append(message.content)
        else:
            return
        #if message.content == 'ping':
        #    await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
BotDiscord = BotDiscord(intents=intents)