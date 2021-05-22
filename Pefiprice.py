import Constants


class Pefiprice:
    bot_channel = {}

    def __init__(self, bot):
        self.bot_channel = {server.id: channel for server in bot.guilds for channel in server.channels
                            if channel.name == Constants.PEFIPRICE_CHANNEL_NAME}
