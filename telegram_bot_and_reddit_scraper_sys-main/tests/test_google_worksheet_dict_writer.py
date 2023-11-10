import asyncio
from src.gspread_sheet_handler import GSpreadSheetHandler
from src.reddit_scraper import RedditScraper
from src import telegram_bot_cls
from src.telegram_bot_cls import TelegramBot
from src.google_worksheet_dict_writer import WorksheetDictWriter
import os


creds_file = "rdantelegrambottest-b35335e97115.json"
gsheet_spreadsheet_name = "1_Hg3se2g1F7wYjnuRznWUKmGhkI4WXGIZajBIJGQd3Q"
tools_gss = GSpreadSheetHandler(credentials_file=creds_file,spreadsheet_name=gsheet_spreadsheet_name, sheet_id=169118404)
tools_gss.wk.get_all_values()
row_num = 1
msg_content_today = tools_gss.get_unshared_item_by_entry_row_num(row_num=row_num).to_dict()
msg_content_today = tools_gss.df.loc[row_num].to_dict()


telegram_bot_name = "RDAN-PrincePills"
telegram_bot_handle = "@rdan_main_bot"
TELEGRAM_BOT_TOKEN = '6536908253:AAFSmE5P_UUhb5sYa_A7WoDXh91fadrQ7UI'
bot = TelegramBot(TELEGRAM_BOT_TOKEN)
GRP_ID = "-1001769336758"
bot_msg_txt = bot.gen_bot_msg(msg_content_today=msg_content_today)
asyncio.run(bot.send(msg=bot_msg_txt, group_chat_id=GRP_ID))


# gss_cls = GSpreadSheetHandler(credentials_file=creds_file,
# 							  spreadsheet_name=gsheet_spreadsheet_name,
# 							  sheet_id=reddit_scraping_test_gsheet_tab_id)

tools_gss = GSpreadSheetHandler(credentials_file=creds_file,spreadsheet_name=gsheet_spreadsheet_name, sheet_id=169118404)

print(f"type(tools_gss): {type(tools_gss)}")


gs_wks = WorksheetDictWriter(tools_gss.gss, list(msg_content_today.keys()))


# reddit_scraper = RedditScraper(client_id=client_id, client_secret=client_secret, user_agent_name=user_agent,
# 							   acc_username=acc_username, acc_password=acc_password)
# res = reddit_scraper.scrape_subreddit_posts(subreddits_cutoff_num=2)



