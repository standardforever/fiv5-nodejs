import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import os
import settings

class GSpreadSheetHandler:
	
	CREDENTIALS_FILE = 'rdantelegrambottest-b35335e97115.json'
	DEF_SPREADSHEET_NAME = '1X9zDWkNRzBI0XTWJ4afYRjQRmpY1OKFhdgcJut5EsTs'
	# DEF_SPREADSHEET_NAME = "1_Hg3se2g1F7wYjnuRznWUKmGhkI4WXGIZajBIJGQd3Q"
	# DEF_SHEET_NAME = 'Sheet1'
	DEF_SHEET_NAME = 'Tools'
	DEF_SHEET_ID = 169118404
	
	def __init__(self, credentials_file=None, spreadsheet_name=None, sheet_name=None, sheet_id=None):
		self.credentials_file_name = credentials_file if credentials_file is not None else GSpreadSheetHandler.DEF_SPREADSHEET_NAME
		self.credentials_file_abs_path = os.path.join(settings.CONFIGS_DIR, self.credentials_file_name)
		self.spreadsheet_name = spreadsheet_name if spreadsheet_name is not None else GSpreadSheetHandler.DEF_SPREADSHEET_NAME
		self.sheet_name = sheet_name if sheet_name is not None else GSpreadSheetHandler.DEF_SHEET_NAME
		self.sheet_id = sheet_id if sheet_id is not None else GSpreadSheetHandler.DEF_SHEET_ID
		
		self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.credentials_file_abs_path)
		
		self.gc = gspread.authorize(self.credentials)
		
		if sheet_id is not None:
			self.gss = self.gc.open_by_key(self.spreadsheet_name)
			self.wk = self.gss.get_worksheet_by_id(self.sheet_id)
			self.df = pd.DataFrame(self.wk.get_all_records())
		else:
			self.gss = self.gc.open_by_key(self.spreadsheet_name)
			self.wk = self.gss.get_worksheet_by_id(self.sheet_id)
			self.df = pd.DataFrame(self.wk.get_all_records())
			
		self.col_headers = self.wk.get_all_values()[0]
		
	def get_unshared_item_by_entry_row_num(self, row_num=0):
		row_num_entry_data = self.df.iloc[row_num]
		return row_num_entry_data
	
	def get_top_most_unshared_row_entry_idx(self):
		unshared_rows = self.df[self.df["Shared"] == "FALSE"]
		top_most_unshared_row_idx = unshared_rows.index.to_list()[0]+1
		top_most_unshared_row_num = top_most_unshared_row_idx + 1
		return top_most_unshared_row_num
	
	def update_row_entry_shared_state(self, row_entry_idx):
		if row_entry_idx > 2:
			gsheet_row_entry_num = row_entry_idx
		else:
			gsheet_row_entry_num = row_entry_idx
		self.wk.update_cell(gsheet_row_entry_num, 7, "TRUE")
		
	def get_row_entry_2_share(self, row_entry_2_share_num):
		if row_entry_2_share_num >= 2:
			row_entry_2_share_idx = row_entry_2_share_num - 2
		else:
			row_entry_2_share_idx = row_entry_2_share_num + 1
		return self.df.iloc[row_entry_2_share_idx]
		

if __name__ == "__main__":
	import time
	
	# gss_cls = GSpreadSheetHandler()
	# gss_cls = GSpreadSheetHandler("rdantelegrambottest-b35335e97115.json")
	creds_file = "rdantelegrambottest-b35335e97115.json"
	gsheet_spreadsheet_name = "1_Hg3se2g1F7wYjnuRznWUKmGhkI4WXGIZajBIJGQd3Q"
	gsheet_sheet_id = 169118404
	gss_cls = GSpreadSheetHandler(credentials_file=creds_file,spreadsheet_name=gsheet_spreadsheet_name, sheet_id=gsheet_sheet_id)
	# time.sleep(5)
	# print(f"type(gss.worksheet): {type(gss.gc)}")
	print(f"type(gss.worksheet): {type(gss_cls.gss)}")
	print(f"type(gss.worksheet): {type(gss_cls.wk)}")
	print(f"type(gss.worksheet): {type(gss_cls.df)}")
	
	gss_cls.get_and_update_top_most_unshared_row_entry()
