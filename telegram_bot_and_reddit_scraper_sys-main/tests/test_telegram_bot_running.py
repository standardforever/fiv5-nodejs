import asyncio
from src.gspread_sheet_handler import GSpreadSheetHandler
from src.reddit_scraper import RedditScraper
from src import telegram_bot_cls
from src.telegram_bot_cls import TelegramBot
from src.google_worksheet_dict_writer import WorksheetDictWriter
import os



telegram_bot_name = "RDAN-PrincePills"
telegram_bot_handle = "@rdan_main_bot"
TELEGRAM_BOT_TOKEN = '6536908253:AAFSmE5P_UUhb5sYa_A7WoDXh91fadrQ7UI'
bot = TelegramBot(TELEGRAM_BOT_TOKEN)
GRP_ID = "-1001769336758"
bot_msg_txt = bot.gen_bot_msg(msg_content_today=msg_content_today)
asyncio.run(bot.send(msg=bot_msg_txt, group_chat_id=GRP_ID))
