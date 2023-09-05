class BotJstore():
    def __init__(self):
        self.__jstore={
            'twitch':[],
            'discord':[]
            }
    def __getTwitch(self):
        return self.__jstore["twitch"][0]
    def __getDiscord(self):
        return self.__jstore["discord"][0]
    def __setDiscord(self, setstr):
        self.__jstore["discord"][0] = setstr
    def __setTwitch(self, setstr):
        self.__jstore["twitch"][0] = setstr