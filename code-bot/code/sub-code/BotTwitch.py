from twitchio.ext import commands

class BotTwitch(commands.Bot):
    def __init__(self, jtokenedit, jchannelsedit, jstore):
        self.__jstore=jstore
        super().__init__(token=jtokenedit, prefix='?', initial_channels=jchannelsedit)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return
        if message.author.name.lower() != self.bot_account_name.lower():
            self.__jstore.__setTwitch(message.content)


#ws=self._ws            
#if len(self.__jstore>0):
#await ws.send_privmsg('jabl3s_ttv',"jabl3s - "+self.jstore.discord[0])
#self.jstore.discord.pop(0)      
