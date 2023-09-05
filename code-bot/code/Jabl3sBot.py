import importlib
import os
from decouple import config
import threading
import queue
import time

class Jabl3sBot:
    def __init__(self):
        self.__thread_run=threading.Thread(target=self.__run)
        self.__subbots={}
        self.__module_folder = "sub-code"
        self.__module_files = [
            f.replace(".py", "")
            for f in os.listdir(self.__module_folder)
            if f.endswith(".py") and not f.startswith("__init__")
        ]
        for module_name in self.__module_files:
            self.__subbots[module_name] = importlib.import_module(f"{self.__module_folder}.{module_name}")
        
        #JSTORE
        self.__jstore=getattr(self.__subbots["BotJstore"],"BotJstore")
        
        #TWITCH
        self.__BOT_TWITCH_TOKEN = config('BOT_TWITCH_TOKEN')
        self.__twitch=getattr(self.__subbots["BotTwitch"],"BotTwitch")(self.__BOT_TWITCH_TOKEN,['jabl3s_ttv'], self.__jstore)
        self.__thread_twitch=threading.Thread(target=self.__twitch.run)
           
        #DISCORD   
        self.__BOT_DISCORD_TOKEN = config('BOT_DISCORD_TOKEN')
        self.__discord_param_queue = queue.Queue()
        self.__discord=getattr(self.__subbots["BotDiscord"],"BotDiscord")(self.__jstore)
        self.__thread_discord=threading.Thread(target=self.__discord.run, args=(self.__discord_param_queue,))
        self.__discord_param_queue.put(self.__BOT_DISCORD_TOKEN)
    def __main(self):
        self.__thread_twitch.start()
        self.__thread_discord.start()
        self.__thread_run.start()
    def __run(self):
            while True:
                time.sleep(2)
                for j in range(0,len(self.__jstore.__getStoreKeys())):
                    if self.__jstore.__getStoreKeys()[j]==self.__jstore.__getStoreValues()[j]:
                        pass
                    else:
                        print(self.__jstore.__getStoreValues()[j])
                        self.__jstore.__getStoreValues()[j]=self.__jstore.__getStoreKeys()[j]
                        
            
if __name__ == "__main__":
     Jabl3sBot().__main()
    


