import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/60b8861dfd2b06491c8af.jpg",
        caption=f"""**Hello \nI แดแด ๐๐๐ใป๐๐๐๐๐พ ๐ฝ๐๐
สแดแด สแดษดแดสแด สส [๐๐๐ ๐๐๐๐๐](https://t.me/NAVYA_KESHRI)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " โฐ๐๐ซ๐จ๐ฎ๐ฉ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญโฑ ", url=f"https://t.me/RcR_OFFICIAL")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "alex", "sushil"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/60b8861dfd2b06491c8af.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " โฐ๐๐ซ๐จ๐ฎ๐ฉ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญโฑ ", url=f"https://t.me/RcR_OFFICIAL")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/60b8861dfd2b06491c8af.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐๐๐ฅ๐ค๐จ๐๐ฉ๐ค๐ง๐ฎ", url=f"https://t.me/LGCY_OFFICIALYT")
                ]
            ]
        ),
    )
