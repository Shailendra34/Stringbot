from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʟʟᴏ {}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ

ᴛʜɪs ʙᴏᴛ ɪs ᴍᴀᴅᴇ ғᴏʀ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ʙᴏᴛʜ. ᴛʜɪs ʙᴏᴛ ɪs 💯 ᴛʀᴜsᴛᴇᴅ ᴀɴᴅ sᴇᴄᴜʀᴇᴅ. ɪᴛ ᴡɪʟʟ ɢᴇɴᴇʀᴀᴛᴇs sᴛʀɪɴɢ ɪɴ ᴍɪɴᴜᴛᴇs. ᴜsᴇ ɪᴛ ʙʏ ᴛᴀᴘᴘɪɴɢ ᴀ ᴄᴏᴍᴍᴀɴᴅ /generate

ʙᴏᴛ ɪs ᴍᴀᴅᴇ ʙʏ @mai_hu_hero ...... 
ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ /generate
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🤟 ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ 💞", callback_data="generate")],
        [InlineKeyboardButton(text="⚜ ʙᴀᴄᴋ ⚜", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🤟 ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ 💞", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🤟 ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ 💞", callback_data="generate")],
        [
            InlineKeyboardButton("❤ ᴏᴡɴᴇʀ 😎", url="https://t.me/mai_hu_hero"), 
            InlineKeyboardButton("🤖 ᴄᴏᴍᴍᴀɴᴅs 🤖", callback_data="help")
        ],
        [InlineKeyboardButton("✌ sᴜᴘᴘᴏʀᴛ & ᴜᴘᴅᴀᴛᴇs ✨", url="https://t.me/modmenumaking")],
    ]

    # Help Message
    HELP = """
⚜ **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs** ⚜

/help - sʜᴏᴡs ʏᴏᴜ ᴛʜɪs ᴍsɢ
/start - sᴛᴀʀᴛs ᴛʜᴇ ʙᴏᴛ
/generate - sᴛᴀʀᴛs ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴘʀᴏᴄᴇss
/cancel - ᴄᴀɴᴄᴇʟs ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛɪɴɢ ᴘʀᴏᴄᴇss
/restart - ʀᴇsᴛᴀʀᴛs ᴛʜᴇ ᴘʀᴏᴄᴇss
"""
