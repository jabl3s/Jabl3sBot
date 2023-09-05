class BotJstore():
    def __init__(self):
        self.__store={
            "twitch":"twitch",
            "discord":"discord"
        }
        self.__keys=self.__store.keys()
        self.__values=self.__store.values()
    def __getStoreKeys(self):
        return self.__keys
    def __getStoreValues(self):
        return self.__values
    def __setDiscord(self, setstr):
        self.__store["discord"] = setstr
    def __setTwitch(self, setstr):
        self.__store["twitch"] = setstr