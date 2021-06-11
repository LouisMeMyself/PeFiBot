import re
import discord
import numpy as np
from cairosvg import svg2png
from constants import Constants


class PefiPic:
    def __init__(self):
        self.hex_regex = re.compile("^[0-9a-fA-F]{6}")
        # PefiLogo
        with open("utils/pefi-logo.svg", "rb") as f:
            self.pefiSVG = f.read().decode("utf-8")
        self.pefi_index = str(self.pefiSVG).find("#E84243;}")
        self.pefiSVG = list(self.pefiSVG)
        # xPefiLogo
        with open("utils/xpefi-logo.svg", "rb") as f:
            self.xpefiSVG = f.read().decode("utf-8")
        self.xpefi_index = str(self.xpefiSVG).find("#FC2736;}")
        self.xpefiSVG = list(self.xpefiSVG)


    def str2hex(self, new_color):
        if new_color.replace(" ", "").replace(",", "") == "":  # handles empty messages
            raise ValueError
        if new_color[0] == "#" and self.hex_regex.match(new_color[1:]) is not None and len(
                new_color) == 7:  # handles the "#XXXXXX" hex colours
            new_color = new_color[1:]
        elif " " in new_color or "," in new_color:
            if " " in new_color and "," in new_color:  # handles the "R,        G,    B" colours
                new_color = new_color.replace(" ", "")
            if "," in new_color:  # handles the "R,G,B" colours
                new_color = np.array(new_color.split(","), dtype=int)
            elif " " in new_color:  # handles the "R G B" colours
                new_color = np.array(new_color.split(" "), dtype=int)
            if isinstance(new_color, np.ndarray) and len(new_color) == 3 and np.any(new_color >= 0) and np.any(
                    new_color <= 255):
                new_color = "%02x%02x%02x" % tuple(new_color)
            else:
                raise ValueError
        if self.hex_regex.match(new_color) is not None and len(new_color) == 6:
            return new_color
        raise ValueError

    def do_profile_picture(self, content):
        try:
            if Constants.PEFI_PICTURE_COMMAND in content:  # Pefi logo
                new_color = str(content.replace(Constants.PEFI_PICTURE_COMMAND, "")[1:])
                self.pefiSVG[self.pefi_index + 1: self.pefi_index + 7] = self.str2hex(new_color)
                svg2png("".join(self.pefiSVG), write_to="utils/pefiPP.png")
                return "Here is your personalized profile picture! 🐧", discord.File("utils/pefiPP.png")

            elif Constants.XPEFI_PICTURE_COMMAND in content:  # xPefi logo
                new_color = str(content.replace(Constants.XPEFI_PICTURE_COMMAND, "")[1:])
                self.xpefiSVG[self.xpefi_index + 1: self.xpefi_index + 7] = self.str2hex(new_color)
                svg2png("".join(self.xpefiSVG), write_to="utils/xpefiPP.png")
                return "Here is your personalized profile picture! 🐧", discord.File("utils/xpefiPP.png")
        except ValueError:
            raise ValueError
        except:
            return "Unexpected error..."