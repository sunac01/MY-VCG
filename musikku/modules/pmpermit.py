from pyrogram import filters
from pyrogram.types import Message

from musikku.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "Merhaba, Bu bir müzik asistanlığı hizmetidir.Lütfen Spam Yapmayın Egellenirsiniz. Destekçi @Azerbesk Lütfen Ona Mesaj Atın!",
   )
    return
