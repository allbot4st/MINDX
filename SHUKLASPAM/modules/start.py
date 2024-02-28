from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("💌 𝐇ᴏᴡ 2 𝐔sᴇ 💡", data="help_back")
    ],
    [
        Button.url("📥 𝐔ᴘᴅᴀᴛᴇs 💸", "https://t.me/I_M_FIGHTER"),
        Button.url("📌 𝐒ᴜᴘᴘᴏʀᴛ 🎀", "https://t.me/CODEX_KA_BAAP_4ST")
    ],
    [
        Button.url("🎀 𝐁ᴀɴᴀʟʟ 𝐒ᴜᴅᴏ ✨", "https://t.me/ll4st_MIND_GAMERII")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [❄𝐌ɪɴᴅ𝐆ᴀᴍᴇʀ⚡](https://t.me/ll4st_MIND_GAMERII)**\n\n"
        TEXT += f"» ** #_4sᴛ sᴘᴀᴍʙᴏᴛ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/c6a2ed96648fd03377dc9.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
