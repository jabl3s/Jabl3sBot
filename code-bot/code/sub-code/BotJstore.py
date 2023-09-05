class BotJstore():
    def __init__(self):
        self.store={
            "twitch":"twitch",
            "discord":"discord"
        }
        self.keys=list(self.store.keys())
        self.values=list(self.store.values())