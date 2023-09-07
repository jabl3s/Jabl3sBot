import discord
from decouple import config
import pika
import threading

class BotDiscord(discord.Client):
    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(config('RABBIT_MQ_URL')))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='Twitch')
        self.channel.queue_declare(queue='Discord')
        self.channel.basic_consume(queue='Twitch',
                      auto_ack=True,
                      on_message_callback=self.on_twitch)
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author.name == "jabl3s":
            self.channel.basic_publish(exchange='',
                routing_key='Twitch',
                body=message.content)
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