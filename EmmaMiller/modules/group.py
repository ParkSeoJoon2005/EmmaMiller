"""
MIT License
Copyright (c) 2021 TheHamkerCat
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os

from pyrogram import filters

from EmmaMiller.function.pluginhelpers import member_permissions
from EmmaMiller import pbot as app


@app.on_message(filters.command("setgtitle") & ~filters.private)
async def set_chat_title(_, message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id
        permissions = await member_permissions(chat_id, user_id)
        if "can_change_info" not in permissions:
            await message.reply_text("You Don't Have Enough Permissions.")
            return
        if len(message.command) < 2:
            await message.reply_text("**Usage:**\n/set_chat_title NEW NAME")
            return
        old_title = message.chat.title
        new_title = message.text.split(None, 1)[1]
        await message.chat.set_title(new_title)
        await message.reply_text(
            f"Successfully Changed Group Title From {old_title} To {new_title}"
        )
    except Exception as e:
        print(e)
        await message.reply_text(e)


@app.on_message(filters.command("settitle") & ~filters.private)
async def set_user_title(_, message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id
        from_user = message.reply_to_message.from_user
        permissions = await member_permissions(chat_id, user_id)
        if "can_change_info" not in permissions:
            await message.reply_text("You Don't Have Enough Permissions.")
            return
        if len(message.command) < 2:
            await message.reply_text(
                "**Usage:**\n/set_user_title NEW ADMINISTRATOR TITLE"
            )
            return
        title = message.text.split(None, 1)[1]
        await app.set_administrator_title(chat_id, from_user.id, title)
        await message.reply_text(
            f"Successfully Changed {from_user.mention}'s Admin Title To {title}"
        )
    except Exception as e:
        print(e)
        await message.reply_text(e)


@app.on_message(filters.command("setgpic") & ~filters.private)
async def set_chat_photo(_, message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id

        permissions = await member_permissions(chat_id, user_id)
        if "can_change_info" not in permissions:
            await message.reply_text("You Don't Have Enough Permissions.")
            return
        if not message.reply_to_message:
            await message.reply_text("Reply to a photo to set it as chat_photo")
            return
        if not message.reply_to_message.photo and not message.reply_to_message.document:
            await message.reply_text("Reply to a photo to set it as chat_photo")
            return
        photo = await message.reply_to_message.download()
        await message.chat.set_photo(photo)
        await message.reply_text("Successfully Changed Group Photo")
        os.remove(photo)
    except Exception as e:
        print(e)
        await message.reply_text(e)
        

@app.on_message(filters.command("setdescription") & ~filters.private)
async def set_chat_description(_, message):
    try:
        chat_id = message.chat.id
        user_id = message.from_user.id
        permissions = await member_permissions(chat_id, user_id)
        if "can_change_info" not in permissions:
            await message.reply_text("You Don't Have Enough Permissions.")
            return
        if len(message.command) < 2:
            await message.reply_text("**Usage:**\n/setdescription NEW NAME")
            return
        new_description = message.text.split(None, 1)[1]
        await message.chat.set_description(new_description)
        await message.reply_text(
            f"Successfully Changed Group Description."
        )
    except Exception as e:
        print(e)
        await message.reply_text(e)
        
__help__ = """
@szrosebot🇱🇰
 ❍ /setgtitle <newtitle>*:* Sets new chat title in your group.
 ❍ /setgpic*:* As a reply to file or photo to set group profile pic!
 ❍ /delgpic*:* Same as above but to remove group profile pic.
 ❍ /setsticker*:* As a reply to some sticker to set it as group sticker set!
 ❍ /setdescription <description>*:* Sets new chat description in group.
"""
__mod_name__ = "💠 GROUP 💠"      
