import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5958312899:AAHiq4rgI9nJF0daMC5af4Wf_off-nQQHR8")

API_ID = int(os.environ.get("API_ID", "16734393"))

API_HASH = os.environ.get("API_HASH", "e49a46ce63b238c429d618c4aa37f52e")

STRING = os.environ.get("STRING", "BQD_WLkAcrBw6ci1KZQHQeEMKvukl11axSfW4kwdyiXSH12Je99jkyEWUCGlW0OGbF6vN1EVrUtr7rW5BpInMmT1YbqyAC37yPrnc9K3QvBV09xVznvXWATobZPiw6ZPQ-wCYUcHakHlM_ik53Gvmh77lnbGjIWAqOcCHAjiOLWVXW37yvtLI3AbqcgO2dubSoZAaoagiNIPMZhHm2EtphLtgo0XWMRmDgNPuA_OfsWaF5SKofm4q-GtOp1fqjBYn5c46xf_V2Pq-xxxDdsC1t9ppgNeRo4to0zbS_JpQbblM43_-BtLzHm_3RgvrmW2d3piUqjEZwm_q4V6CjzorYWnuTZ62QAAAABOHUhrAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
