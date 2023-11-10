import asyncio
from src.gspread_sheet_handler import GSpreadSheetHandler
from src.reddit_scraper import RedditScraper
from src.telegram_bot_cls import TelegramBot


def run(gsheet_creds_dict: dict = None, telegram_bot_creds_dict: dict = None) -> None:
	if gsheet_creds_dict is None:
		gsheet_creds = {
			"credentials_file": "rdantelegrambottest-b35335e97115.json",
			"spreadsheet_name": "1_Hg3se2g1F7wYjnuRznWUKmGhkI4WXGIZajBIJGQd3Q",
			"sheet_id": 169118404
			}
	
	if telegram_bot_creds_dict is None:
		telegram_bot_creds = {
			"telegram_bot_name" :"RDAN-PrincePills",
			"telegram_bot_handle" :"@rdan_main_bot",
			"TELEGRAM_BOT_TOKEN" :'6536908253:AAFSmE5P_UUhb5sYa_A7WoDXh91fadrQ7UI',
			"GRP_ID":"-1001769336758"
			}
	
	gss_cls = GSpreadSheetHandler(credentials_file=gsheet_creds["credentials_file"],
								  spreadsheet_name=gsheet_creds["spreadsheet_name"],
								  sheet_id=gsheet_creds["sheet_id"])
	
	bot = TelegramBot(telegram_bot_creds["TELEGRAM_BOT_TOKEN"])
	
	top_most_unshared_row_num = gss_cls.get_top_most_unshared_row_entry_idx()
	top_most_unshared_row = gss_cls.get_row_entry_2_share(row_entry_2_share_num=top_most_unshared_row_num)
	msg_content_today = top_most_unshared_row.to_dict()
	bot_msg_txt = bot.gen_bot_msg(msg_content_today=msg_content_today)
	asyncio.run(bot.send(msg=bot_msg_txt, group_chat_id=telegram_bot_creds["GRP_ID"]))
	gss_cls.update_row_entry_shared_state(row_entry_idx=top_most_unshared_row_num)
	
	
if __name__ == "__main__":
	import asyncio
from src.gspread_sheet_handler import GSpreadSheetHandler
from src.reddit_scraper import RedditScraper
from src import telegram_bot_cls
from telegram_bot_cls import TelegramBot
from src.google_worksheet_dict_writer import WorksheetDictWriter
import os

creds_file = "rdantelegrambottest-b35335e97115.json"
# reddit_scraping_test_gsheet_tab_id = 373474331  # RedditScrapingTest
reddit_scraping_test_gsheet_tab_id = 169118404  # Tools
# gsheet_spreadsheet_name = "1_Hg3se2g1F7wYjnuRznWUKmGhkI4WXGIZajBIJGQd3Q"
gsheet_spreadsheet_name = "1_Hg3se2g1F7wYjnuRznWUKmGhkI4WXGIZajBIJGQd3Q"
gss_cls = GSpreadSheetHandler(credentials_file=creds_file,
							  spreadsheet_name=gsheet_spreadsheet_name,
							  sheet_id=reddit_scraping_test_gsheet_tab_id)

tools_gss = GSpreadSheetHandler(credentials_file=creds_file,spreadsheet_name=gsheet_spreadsheet_name,
							  sheet_id=169118404)
test_gss = GSpreadSheetHandler(credentials_file=creds_file,spreadsheet_name=gsheet_spreadsheet_name,
							  sheet_id=373474331)
tools_gss.wk.get_all_values()
# test_gss.wk.update(('A2:K2', [[42], [43]]))
# sheet_id=373474331)
# sheet_id=169118404)

# client_id = "WcRkVk7z-cQwYLhAKNjaWQ"
client_id = "eZFjnh49umrJLDSorGzipw"
# client_secret = "cib6QCNBQ4N2EpH7h7jNQ0B9aMEcIw"
client_secret = "adOW43bU5HVRnyihkqO12ZWTUus6mw"
# user_agent = "rdan_agg"
user_agent = "rdan_rddt_app"

# acc_username = "RDANReddit"
# acc_password = "Zm2m09&S#r_3dl[f)sFRI"

acc_username = "RDAN-Tech"
acc_password = "Zm2m09&S#r_3dl[f)sFR"

# acc_username = "RDANReddit"
# acc_password = "RDANdutchDEPLOYEDeuDISTRIBUTED"

reddit_scraper = RedditScraper(client_id=client_id, client_secret=client_secret, user_agent_name=user_agent,
							   acc_username=acc_username, acc_password=acc_password)
res = reddit_scraper.scrape_subreddit_posts(subreddits_cutoff_num=2)



telegram_bot_name = "RDAN-PrincePills"
telegram_bot_handle = "@rdan_main_bot"
# TELEGRAM_BOT_TOKEN = '353694r8253:AAFSmE5P_UUhb5sYa_A7WoD5h91fadrQ7UI'
# TELEGRAM_BOT_TOKEN = '6536908253:AAFSmE5P_UUhb5sYa_A7WoDXh91fadrQ7UI'
# TELEGRAM_BOT_TOKEN = '6536908253:AAFSmE5P_UUhb5sYa_A7WoDXh91fadrQ7UI'

# TELEGRAM_BOT_TOKEN = '6536908253:AAFSmE5P_UUhb5sYa_A7WoDXh91fadrQ7UI'
# bot = TelegramBot(TELEGRAM_BOT_TOKEN)
# GRP_ID = "-1001717303743"
# asyncio.run(bot.send(msg=bot_msg_txt, group_chat_id=GRP_ID))

# bot = TelegramBot(TELEGRAM_BOT_TOKEN)
# bot = telegram_bot_cls.TelegramBot(TELEGRAM_BOT_TOKEN)
# bot = TelegramBot(TELEGRAM_BOT_TOKEN)
TELEGRAM_BOT_TOKEN = '6536908253:AAFSmE5P_UUhb5sYa_A7WoDXh91fadrQ7UI'
bot = TelegramBot(TELEGRAM_BOT_TOKEN)
# GRP_ID = "-1001717303743"
GRP_ID = "-1001769336758"

# msg_content_today = {'Date': '2021-09-06', "Title": "Test Title", "Description": "Test Description", "URL": "Test URL", "Topics": "Test Topics", "Type": "Test Type"}
row_num = 1
msg_content_today = tools_gss.get_unshared_item_by_entry_row_num(row_num=row_num).to_dict()
msg_content_today = tools_gss.df.loc[row_num].to_dict()

bot_msg_txt = bot.gen_bot_msg(msg_content_today=msg_content_today)

asyncio.run(bot.send(msg=bot_msg_txt, group_chat_id=GRP_ID))

subreddit_name = "MachineLearning"
post_row_num = 1
reddit_post = [i for i in res[subreddit_name].values()][post_row_num]
entry_data = [reddit_post[key] for key in list([i for i in res[subreddit_name].values()][post_row_num].keys())]
for k, v in reddit_post.items():
	reddit_post[k] = str(v)
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
row_num = 2
for k, v in reddit_post.items():
	letter = letters[list(reddit_post.keys()).index(k)]
	test_gss.wk.update(f'{letter}{row_num}', v)
test_gss.wk.update(f'A{row_num}:K{row_num}', entry_data)
# test_gss.wk.update(('A2:K2', [reddit_post["title"],
# 							  reddit_post["title"],
# 							  reddit_post["title"],
# 							  reddit_post["title"],
# 							  reddit_post["title"],
# 							  reddit_post["title"],
# 							  reddit_post["title"]]))


# GRP_ID = "-1001715302743"
# GRP_ID = "-1950393078"
# GRP_ID = "-1769336758"
# GRP_ID = "-1769336758"
# GRP_ID = "-1769336758_1"
# GRP_ID = "-1769336758_2"

# GRP_ID = "-1717303743"
# msg_content_today = {'Date': '2021-09-06', "Title": "Test Title",
# 					 "Description": "Test Description", "URL": "Test URL",
# 					 "Topics": "Test Topics", "Type": "Test Type"}
# bot_msg_txt = bot.gen_bot_msg(msg_content_today)
# asyncio.run(bot.send(msg=bot_msg_txt, group_chat_id=GRP_ID))
#
# gs_wks = WorksheetDictWriter(gss_cls.gss, list(msg_content_today.keys()))
#
# msg_content_today_2 = {'Date': '2021-09-06', "Title": "Test Title 2",
# 					   "Description": "Test Description 2", "URL": "Test URL 2",
# 					   "Topics": "Test Topics 2", "Type": "Test Type 2"}
# gs_wks.writerow(msg_content_today_2)
# gs_wks.current_row += 1
# gs_wks.column = 1
# gs_wks.writerow(msg_content_today_2)
