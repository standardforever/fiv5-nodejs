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
			"GRP_ID":"-1001950393078"
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
	run()
