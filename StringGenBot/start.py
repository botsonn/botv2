from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝐇𝐞𝐲 {msg.from_user.mention}🍷,

𝐈 𝐀𝐦 {me2},
انا بوت  توليد جلسات البايروجرام 1 .
والبايرجرامv2.
وجلسات الترمكس بشكل امن بوت سورس نجد 🇸🇦.

Dev🏅  : [𝒏𝒂𝒋𝒅 🇸🇦](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text=" استخراج ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton(" 𝒔𝒐𝒖𝒓𝒄𝒆 𝒏𝒂𝒋𝒅 🇸🇦", url="https://t.me/ngd_1"),
                    InlineKeyboardButton("َقناة السورس 𓏺", url="https://t.me/ngd_5")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
