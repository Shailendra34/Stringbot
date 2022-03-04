from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ {}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}
ʙᴏᴛ ғᴏʀ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴄʀᴇᴀᴛᴇ sᴇssɪᴏɴ.
[➼]sᴏ ᴡʜᴀᴛ ᴜ ᴡᴀɪᴛɪɴɢ ғᴏʀ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ
───────────────────────

ɪғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜsᴛ ᴛʜɪs ʙᴏᴛ, 
1) sᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪs ᴍᴇssᴀɢᴇ
2) ᴅᴇʟᴇᴛᴇ ᴛʜɪs ᴄʜᴀᴛ

───────────────────────
sᴛɪʟʟ ʀᴇᴀᴅɪɴɢ ?
ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ. ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ... 

💞 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 💞: [ʜᴇʀᴏ](https://t.me/HeroOfficialBots)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🌸 𝙎𝙩𝙖𝙧𝙩 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙞𝙣𝙜 𝙎𝙚𝙨𝙨𝙞𝙤𝙣 ✨", callback_data="generate")],
    ]

    generate_button = [
        [InlineKeyboardButton("🌸 𝙎𝙩𝙖𝙧𝙩 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙞𝙣𝙜 𝙎𝙚𝙨𝙨𝙞𝙤𝙣 ✨", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🌸 𝙎𝙩𝙖𝙧𝙩 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙞𝙣𝙜 𝙎𝙚𝙨𝙨𝙞𝙤𝙣 ✨", callback_data="generate")],
        [InlineKeyboardButton("💐 𝙈𝙤𝙧𝙚 𝘽𝙤𝙩𝙨 ✨", url="https://t.me/HeroOfficialBots")],
        [
            InlineKeyboardButton("⚜ 𝙃𝙤𝙬 𝙩𝙤 𝙐𝙨𝙚 ⚜", callback_data="help"),
            InlineKeyboardButton("🤟 𝘼𝙗𝙤𝙪𝙩 😎", callback_data="about")
        ],
        [InlineKeyboardButton("💝 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 ✨", url="https://t.me/DeeCodeBots")],
    ]

    # Help Message
    HELP = """
✨ **𝘼𝙫𝙖𝙞𝙡𝙖𝙗𝙡𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨** ✨

/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ
/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/generate - sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
/restart - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
"""

    # About Message
    ABOUT = """
**𝘼𝙗𝙤𝙪𝙩 𝙏𝙝𝙞𝙨 𝘽𝙤𝙩** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @HeroOfficialBots

ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀ : @HeroOfficialBots
    """
