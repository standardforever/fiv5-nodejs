import asyncio
from src.gspread_sheet_handler import GSpreadSheetHandler
from src.reddit_scraper import RedditScraper
from src import telegram_bot_cls
from src.telegram_bot_cls import TelegramBot
from src.google_worksheet_dict_writer import WorksheetDictWriter
import os



client_id = "eZFjnh49umrJLDSorGzipw"
client_secret = "adOW43bU5HVRnyihkqO12ZWTUus6mw"
user_agent = "rdan_rddt_app"
acc_username = "RDAN-Tech"
acc_password = "Zm2m09&S#r_3dl[f)sFR"


reddit_scraper = RedditScraper(client_id=client_id, client_secret=client_secret,
							   user_agent_name=user_agent, acc_username=acc_username,
							   acc_password=acc_password)

# res = reddit_scraper.scrape_subreddit_posts(subreddits_cutoff_num=2)
res = reddit_scraper.scrape_subreddit_posts(top_num_x=1, subreddits_cutoff_num=1)


print(f"res: {res}")
print(f"type(res): {type(res)}")
