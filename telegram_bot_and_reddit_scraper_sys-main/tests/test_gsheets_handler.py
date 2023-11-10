import asyncio
from src.gspread_sheet_handler import GSpreadSheetHandler
from src.reddit_scraper import RedditScraper
from src import telegram_bot_cls
from src.telegram_bot_cls import TelegramBot
from src.google_worksheet_dict_writer import WorksheetDictWriter
import os


creds_file = "rdantelegrambottest-b35335e97115.json"
gsheet_spreadsheet_name = "1_Hg3se2g1F7wYjnuRznWUKmGhkI4WXGIZajBIJGQd3Q"
tools_gss = GSpreadSheetHandler(credentials_file=creds_file,spreadsheet_name=gsheet_spreadsheet_name,
sheet_id=169118404)
tools_gss.wk.get_all_values()
row_num = 1
msg_content_today = tools_gss.get_unshared_item_by_entry_row_num(row_num=row_num).to_dict()
msg_content_today = tools_gss.df.loc[row_num].to_dict()


print(f"rcol_headers: {tools_gss.col_headers}")
