import Config
import logging
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
    ":memory:",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="Stringbot"),
)

app.storage.SESSION_STRING_FORMAT = ">B?256sQ?"

# Run Bot

    app.start()
    print("sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ...")
    idle()
    app.stop()
    print("ʙᴏᴛ sᴛᴏᴘᴘᴇᴅ...")
