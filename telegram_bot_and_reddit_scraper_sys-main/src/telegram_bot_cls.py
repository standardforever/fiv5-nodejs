from prettytable import PrettyTable
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
import telegram
# from telegram import ParseMode
from telegram.constants import ParseMode
# import asyncio
import requests
# import json

class TelegramBot:
    
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.bot = telegram.Bot(token=self.bot_token)
    
    
    async def send(self, msg, group_chat_id):
        """
        Send a message "msg" to a telegram user or group specified by "chat_id"
        :param msg: Text of the message to be sent. Max 4096 characters after entities parsing.
        :type msg: str
        :param group_chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type group_chat_id: int|str
        :param token: Bot's unique authentication token.
        :type token: str
        :return:
        :rtype:
        """
        # await self.bot.sendMessage(chat_id=group_chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)
        # await self.bot.sendMessage(chat_id=group_chat_id, text=msg, parse_mode=ParseMode.HTML)
        await self.bot.sendMessage(chat_id=group_chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)
        # await self.bot.sendMessage(chat_id=group_chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)
        # asyncio.run(send(msg=MessageString, group_chat_id=GRP_ID, token=TELEGRAM_BOT_TOKEN))
        # await self.bot.sendMessage(chat_id=group_chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)
    
    def get_rdam_current_weather(self):
        BASE_URL = "https://wttr.in/Rotterdam?format=4"
        res = requests.get(BASE_URL).content.decode().strip()
        formatted_res = (res.replace("   ", "|")
                         .replace("C ", "C|")
                         .replace(": ", ":")
                         .split(":")[-1].strip())
        return formatted_res
    
    
    def gen_msg_table(self, date, weather):
        table = PrettyTable()
        table.title = "Rotterdam Today"
        table.field_names = ["Date", "Weather"]
        table.add_row([date, weather])
        response = '```\n{}```'.format(table.get_string())
        return response
    
    
    def gen_bot_msg(self, msg_content_today):
        """
        Generate a message to be sent by the bot
        :param msg_content_today: A dictionary containing the message content
        with keys: ["Date", "Title", "Description", "URL", "Topics", "Type"]
        :type msg_content_today: dict
        """
        rdam_current_weather = self.get_rdam_current_weather()
        msg_table = self.gen_msg_table(msg_content_today['Date'], rdam_current_weather)
        msg_header = "     Tip/News of the day!     "
        msg_div = "~" * len(msg_header.lstrip().rstrip())
        MessageString = (f"*{msg_header}*"
                         f"\nRotterdam Today ({msg_content_today['Date']})"
                         f"\nWeather: {rdam_current_weather}"
                         f"\n"
                         f"\n_{msg_content_today['Title']}_"
                         f"\n{msg_content_today['Description']}"
                         f"\n"
                         f"\nURL: {msg_content_today['URL']}"
                         f"\n"
                         f"\nTopics: {msg_content_today['Topics']}"
                         f"\nType: {msg_content_today['Type']}"
                         f"\n")
        return MessageString
    
# if __name__ == '__main__':
#     # TELEGRAM_BOT_TOKEN = '6536908253:AAFSmE5P_UUhb5sYa_A7WoDXh91fadrQ7UI'
#     TELEGRAM_BOT_TOKEN = '6536908253:AAFSmE5P_UUhb5sYa_A7WoDXh91fadrQ7UI'
#     bot = TelegramBot(TELEGRAM_BOT_TOKEN)
#     GRP_ID = "-1001717303743"
#     bot_msg_txt = bot.gen_bot_msg(msg_content_today={'Date': '2021-09-06', "Title": "Test Title", "Description": "Test Description", "URL": "Test URL", "Topics": "Test Topics", "Type": "Test Type"})
#     asyncio.run(bot.send(msg=bot_msg_txt, group_chat_id=GRP_ID))
#     # E.g. output
#     # Tip/News of the day!
#     # Rotterdam Today (2021-09-06)
#     # Weather: 🌦|🌡️+23°C|🌬️→7km/h
#     #
#     # Test Title
#     # Test Description
#     #
#     # URL: Test URL
#     #
#     # Topics: Test Topics
#     # Type: Test Type
