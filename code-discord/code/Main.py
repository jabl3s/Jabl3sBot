import importlib
import os
from decouple import config

def main():
    # Read environment variables from the .env file
    BOT_DISCORD_TOKEN = config('BOT_DISCORD_TOKEN')
    bot={}
    # Specify the folder containing your modules
    module_folder = ""
    # Get a list of all Python files in the subfolder (excluding __init__.py)
    module_files = [
        f.replace(".py", "")
        for f in os.listdir(module_folder)
        if f.endswith(".py") and not f.startswith("__init__")
    ]
    # Dynamically import the modules
    for module_name in module_files:
        bot[module_name] = importlib.import_module(f"{module_name}") ### {module_folder}.

    getattr(bot["BotDiscord"],"BotDiscord").run(BOT_DISCORD_TOKEN)

if __name__ == "__main__":
    main()

