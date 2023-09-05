import sys
import os
import time
import importlib
from decouple import config
import threading
import queue


class Jabl3sBot:
    def __init__(self):
        self.thread_run=threading.Thread(target=self.__run)
        self.subbots={}
        self.module_folder = "sub-code"
        self.module_files = [
            f.replace(".py", "")
            for f in os.listdir(self.module_folder)
            if f.endswith(".py") and not f.startswith("__init__")
        ]
        for module_name in self.module_files:
            self.subbots[module_name] = importlib.import_module(f"{self.module_folder}.{module_name}")
        
        #JSTORE
        self.jstore=getattr(self.subbots["BotJstore"],"BotJstore")()
        
        #TWITCH
        BOT_TWITCH_TOKEN = config('BOT_TWITCH_TOKEN')
        self.twitch=getattr(self.subbots["BotTwitch"],"BotTwitch")(BOT_TWITCH_TOKEN,['jabl3s_ttv'], self.jstore)
        self.thread_twitch=threading.Thread(target=self.twitch.run)
           
        #DISCORD   
        BOT_DISCORD_TOKEN = config('BOT_DISCORD_TOKEN')
        discord_param_queue = queue.Queue()
        self.discord=getattr(self.subbots["BotDiscord"],"BotDiscord")(self.jstore)
        discord_param_queue.put(BOT_DISCORD_TOKEN)
        self.thread_discord=threading.Thread(target=self.discord.run, args=(discord_param_queue,))
    
    def main(self):
        self.thread_twitch.start()
        self.thread_discord.start()
        self.thread_run.start()
    
    def __run(self):
            while True:
                time.sleep(2)
                for j in range(0,len(self.jstore.keys)):
                    if self.jstore.keys[j]==self.jstore.values[j]:
                        pass
                    else:
                        print(self.jstore.values[j])
                        self.jstore.values[j]=self.jstore.keys[j]
                        sys.stdout.flush()
                                
if __name__ == "__main__":
     Jabl3sBot().main()
    


