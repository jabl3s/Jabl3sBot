import importlib
import os
from decouple import config
import threading
def main():
    bot={}
    # Read environment variables from the .env file
    BOT_TWITCH_TOKEN = config('BOT_TWITCH_TOKEN')
    BOT_DISCORD_TOKEN = config('BOT_DISCORD_TOKEN')
    # Specify the folder containing your modules
    module_folder = "sub-code"
    # Get a list of all Python files in the subfolder (excluding __init__.py)
    module_files = [
        f.replace(".py", "")
        for f in os.listdir(module_folder)
        if f.endswith(".py") and not f.startswith("__init__")
    ]
    # Dynamically import the modules
    for module_name in module_files:
        bot[module_name] = importlib.import_module(f"{module_folder}.{module_name}")
    jstore=getattr(bot["BotJstore"],"BotJstore")
    thread_twitch=threading.Thread(target=getattr(bot["BotTwitch"],"BotTwitch")(BOT_TWITCH_TOKEN,['jabl3s_ttv'],jstore).run())
    thread_discord=threading.Thread(target=getattr(bot["BotDiscord"],"BotDiscord")(jstore).run(BOT_DISCORD_TOKEN))
    thread_twitch.start()
    thread_discord.start()
    
if __name__ == "__main__":
    main()
    


