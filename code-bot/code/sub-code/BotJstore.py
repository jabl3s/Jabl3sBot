class BotJstore():
    def __init__(self):
        self.store={
            "twitch":"twitch",
            "discord":"discord"
        }
        self.keys=list(self.store.keys())
        self.values=list(self.store.values())
    def getStoreKeys(self):
        return self.keys
    def getStoreValues(self):
        return self.values
    def setDiscord(self, setstr):
        self.store["discord"] = setstr
    def setTwitch(self, setstr):
        self.store["twitch"] = setstr