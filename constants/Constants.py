import json

PEFI_PICTURE_COMMAND = "!pefipic"
IPEFI_PICTURE_COMMAND = "!ipefipic"
XPEFI_PICTURE_COMMAND = "!xpefipic"

IPEFI_ADDRESS = "0xE9476e16FE488B90ada9Ab5C7c2ADa81014Ba9Ee"

# ABI for web3
try:
    with open("utils/ipefiabi.json", "r") as f:
        IPEFI_ABI = json.load(f)
except:
    IPEFI_ABI = None

# PEFIPIC_CHANNEL_ID = 840324108113281034  # test server
# PEFIPRICE_CHANNEL_ID = 852869505785135174  # test server
PEFIPRICE_CHANNEL_ID = (842285016695832576, 827679024565846057)
PEFIPIC_CHANNEL_ID = 840375343406907402
PANGO_API_URL = "https://api.thegraph.com/subgraphs/name/dasconnor/pangolin-dex"

ERROR_ON_PEFIPIC = """How to use pefipic for profile pictures:

1. Choose a HEX color or a RGB color in these formats: `#00FFFF`, `00FFFF`, `0 255 255` or `0,255,255` [(color picker)](https://htmlcolorcodes.com/color-picker/)

2. Enter this command `!pefipic [color]`, `!xpefipic [color]` or `!ipefipic [color]` with your selected color."""
