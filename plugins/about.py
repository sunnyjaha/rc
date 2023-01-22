import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','5958312899:AAHiq4rgI9nJF0daMC5af4Wf_off-nQQHR8')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Total User:- {total_user()}\nBot :- @rename_amrobot\nBuy Subscription :- @AmRobots_Bots\nSubscribe :- https://youtube.com/@amrobots\n\nTotal Renamed File :-{total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} ",quote=True)
