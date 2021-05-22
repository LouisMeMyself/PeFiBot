import discord

import Constants
from Pefipic import Pefipic
from Pefiprice import Pefiprice
from Pefireact import Pefireact


class Pefibot:
    pefipic = Pefipic
    # pefireact = Pefireact  #currently it's useless
    # pefiprice = Pefiprice  #currently it's are useless

    def __init__(self, bot):
        print('PefiBot have logged in as {0.user}'.format(bot))
        self.pefipic = Pefipic(bot)
        # self.pefireact = Pefireact(bot)
        # self.pefiprice = Pefiprice(bot)

    def do_profile_picture(self, content):
        return self.pefipic.do_profile_picture(content)



