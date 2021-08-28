from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAECNFZhI8kJRPUvPzAO8dzVJppN0OOAHQACRQIAAr\_sqVQp8T9O6Mf0eSAE")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [NORA](https://t.me/rosebakthan).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Commands", url="https://telegra.ph/NORA-VC-PLAYER-08-28")
                  ],[
                    InlineKeyboardButton(
                        "Devloper", url="https://t.me/rosebakthan"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Malayalam_Chatting_Links"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Noravc_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**NORA Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "contact dev", url="https://t.me/rosebakthan")
                ]
            ]
        )
   )


