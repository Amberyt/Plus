import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
import asyncio
import shutil
from userbot import AUTOPIC_COMMENT, AUTOPIC_COLOUR

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
AUTOPIC_STR = str(AUTOPIC_COMMENT) if AUTOPIC_COMMENT else "Life Is too Short.\n And so is TG account."

@command(pattern="^.autopic", outgoing=True)
async def autopic(event):
    await event.edit("**Autopic** has been Enabled!!")
    downloaded_file_name = "userbot/original_pic.png"
    downloader = SmartDL(Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    photo = "userbot/photo_pfp.png"
    while not downloader.isFinished():
        place_holder = None
    counter = -0
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime(f"Time: %H:%M \nDate: %d.%m.%y \n{AUTOPIC_STR}")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((95, 250), current_time, font=fnt, fill=(f{AUTOPIC_COLOUR}))
        img.save(photo)
        file = await bot.upload_file(photo)  # pylint:disable=E0602
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            counter -= 0
            await asyncio.sleep(60)
        except:
            return
