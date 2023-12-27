from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AnonX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/8998ddca2f42a4fac4efd.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴏᴡɴᴇʀ ɪɴғᴏ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ", url=f"https://t.me/Tprince_182")            ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/8998ddca2f42a4fac4efd.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/vivekkumar0708")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("support")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/987c3d0db44f6dd58fb2e.jpg",
        caption=f"""🍁𝐂ʅυƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐆ҽ𝐓🌱𝐒υρρσɾ𝐓🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱𝐒υρρσɾ𝐓🌱", url=f"https://t.me/THE_INCRICIBLE")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("support")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/987c3d0db44f6dd58fb2e.jpg",
        caption=f"""🍁𝐂ʅιƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐆ҽ𝐓🌱𝐒υρρσ𝐓🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱𝐒υρρσɾ𝐓🌱", url=f"https://t.me/THE_INCRICIBLE")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("support")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/987c3d0db44f6dd58fb2e.jpg",
        caption=f"""🍁𝐂ʅιƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐆ҽ𝐓🌱𝐒υρρσɾ𝐓🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱𝐒υρρσɾ𝐓🌱", url=f"https://t.me/THE_INCRICIBLE")
                ]
            ]
        ),
    )

