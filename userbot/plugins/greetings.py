import asyncio
from uniborg.util import admin_cmd

DEL_TIMEOUT = 5

@borg.on(admin_cmd(pattern="gn"))
async def gn(event):
    await event.edit("｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･")
    await asyncio.sleep(DEL_TIMEOUT)
    await event.delete()
    

@borg.on(admin_cmd(pattern="gm"))
async def gm(event):
    await event.edit("｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･")
    await asyncio.sleep(DEL_TIMEOUT)
    await event.delete()


@borg.on(admin_cmd(pattern="like"))
async def like(event):
    await event.edit("👍🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👍🏿\n👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿\n👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👉🏼👉🏻❤👈🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿\n👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿\n👍🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👍🏿")
    await asyncio.sleep(DEL_TIMEOUT)
    await event.delete()
