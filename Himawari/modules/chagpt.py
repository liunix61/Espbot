from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from config import *
import openai
openai.api_key = OPENAI_API

@Client.on_message(filters.private & filters.text)
async def lazy_answer(client, message):
    if AI == True: 
        user_id = message.from_user.id
        if user_id:
            try:
                lazy_users_message = message.text
                user_id = message.from_user.id
                response = openai.Completion.create(
                    model = "text-davinci-003",
                    prompt = lazy_users_message,
                    temperature = 0.5, 
                    max_tokens = 1000,
                    top_p=1,
                    frequency_penalty=0.1,
                    presence_penalty = 0.0,
                )
                btn=[
                        [InlineKeyboardButton(text=f"⇱🤷‍♀️ Take Action 🗃️⇲", url=f'https://t.me/{temp.U_NAME}')],
                        [InlineKeyboardButton(text=f"🗑 Delete log ❌", callback_data=f'close_data')],
                    ]
                reply_markup=InlineKeyboardMarkup(btn)
                footer_credit = "Enjoy with Ath's Chat Gpt Integrated  Bot "
                lazy_response = response.choices[0].text 
                await client.send_message(LAZY_AI_LOGS, text=f"⚡️⚡️#Lazy_AI_Query \n\n• A user named **{message.from_user.mention}** with user id - `{user_id}`. Asked me this query...\n\n══❚█══Q   U   E   R   Y══█❚══\n\n\n[Q྿.]**{lazy_users_message}**\n\n👇Here is what i responded:\n:-`{lazy_response}`\n\n\n❚═USER ID═❚═• `{user_id}` \n❚═USER Name═❚═• `{message.from_user.mention}` \n\n🗃️" , reply_markup = reply_markup )
                await message.reply(f"{lazy_response}\n\n\n{footer_credit}")
            except Exception as error:
                print(error)
    else:
        return
   