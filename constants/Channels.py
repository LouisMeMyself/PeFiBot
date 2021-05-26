from constants import Constants


class Channels:
    def __init__(self, bot):
        self.profile_picture = {server.id: channel for server in bot.guilds for channel in server.channels
                           if channel.name == Constants.PEFIPIC_CHANNEL_NAME}
