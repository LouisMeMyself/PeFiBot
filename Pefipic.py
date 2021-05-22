import re
import discord
import numpy as np
from cairosvg import svg2png
import Constants

class Pefipic:
    bot_channel = {}
    def __init__(self, bot):
        self.bot_channel = {server.id: channel for server in bot.guilds for channel in server.channels
                            if channel.name == Constants.PEFIPIC_CHANNEL_NAME}
        self.hex_regex = re.compile("^[0-9a-fA-F]{6}")
        with open("ProfilePictureDiscordSVG.svg", "rb") as f:
            self.PeFisvg = f.read().decode("utf-8")
        self.index = str(self.PeFisvg).find("#E84243")
        self.PeFisvg = list(self.PeFisvg)

    def do_profile_picture(self, content):
        try:
            new_color = str(content.replace(Constants.PROFILE_PICTURE_COMMAND, "")[1:])
            if new_color.replace(" ", "").replace(",", "") == "":
                return "Please write a HEX color or a RGB color. in these formats: '#00FFFF', '00FFFF', '0 255 255' or '0,255,255"
            if new_color[0] == "#" and self.hex_regex.match(new_color[1:]) is not None and len(new_color) == 7:
                new_color = new_color[1:]
            elif " " in new_color or "," in new_color:
                if " " in new_color:
                    new_color = np.array(new_color.split(" "), dtype=int)
                elif "," in new_color:
                    new_color = np.array(new_color.split(","), dtype=int)
                if isinstance(new_color, np.ndarray) and len(new_color) == 3 and np.any(new_color >= 0) and np.any(new_color <= 255):
                    new_color = "%02x%02x%02x" % tuple(new_color)
                else:
                    return "RGB colours are between 0 and 255 and need 3 integers, like '127 255 212' or '127,255,212'"
            if self.hex_regex.match(new_color) is not None and len(new_color) == 6:
                self.PeFisvg[self.index+1: self.index + 7] = new_color
                svg2png("".join(self.PeFisvg), write_to="PeFi_PP.png")
                return "Here is your personalized profile picture! 🐧", discord.File("PeFi_PP.png")
            else:
                return "Please write a HEX color or a RGB color. in these formats: '#00FFFF', '00FFFF', '0 255 255' or '0,255,255"
        except ValueError:
            return "Please write a HEX color or a RGB color. in these formats: '#00FFFF', '00FFFF', '0 255 255' or '0,255,255"
        except:
            return "Unexpected error..."