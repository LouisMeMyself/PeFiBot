import Constants

class Pefireact:
    bot_channel = {}

    def __init__(self, bot):
        self.bot_channel = {server.id: channel for server in bot.guilds for channel in server.channels
                            if channel.name == Constants.PEFIREACT_CHANNEL_NAME}