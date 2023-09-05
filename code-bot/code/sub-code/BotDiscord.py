import discord

class BotDiscord(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author.name == "jabl3s":
            print("jabl3s: ", message.content)
        else:
            return
        #if message.content == 'ping':
        #    await message.channel.send('pong')
    async def on_twitch(self, ch, method, properties, body):
        channel = self.get_channel(1148445315326820373)
        await channel.send(body)

intents = discord.Intents.default()
intents.message_content = True
BotDiscord = BotDiscord(intents=intents)