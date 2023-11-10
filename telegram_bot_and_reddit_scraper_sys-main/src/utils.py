import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def get_gsheet(spreadsheet_name=None, sheet_name=None, sheet_id=None):
	
	CREDENTIALS_FILE = 'rdantelegrambottest-b35335e97115.json'
	
	if spreadsheet_name is None:
		SPREADSHEET_NAME = '1X9zDWkNRzBI0XTWJ4afYRjQRmpY1OKFhdgcJut5EsTs'
	else:
		SPREADSHEET_NAME = spreadsheet_name
	
	if sheet_name is None:
		SHEET_NAME = 'Sheet1'
	else:
		SHEET_NAME = sheet_name
	
	if sheet_id is None:
		SHEET_ID = 169118404
	else:
		SHEET_ID = sheet_id
	
	credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE)
	gc = gspread.authorize(credentials)
	print(f"type(gc): {type(gc)}")
	if SHEET_ID is not None:
		print(f"type(gc.open_by_key(SPREADSHEET_NAME)): {type(gc.open_by_key(SPREADSHEET_NAME))}")
		worksheet = gc.open_by_key(SPREADSHEET_NAME).get_worksheet_by_id(SHEET_ID)
	else:
		worksheet = gc.open(SPREADSHEET_NAME).worksheet(SHEET_NAME)
	
	ss = gc.open_by_key(SPREADSHEET_NAME)
	return worksheet


def get_gsheet_df(spreadsheet_name=None, sheet_name=None, sheet_id=None):
	ss = get_gsheet(spreadsheet_name=spreadsheet_name, sheet_id=sheet_id)
	df = pd.DataFrame(ss.get_all_records())
	return df


def find_deepest(data):
	if not any([isinstance(data.get(k), dict) for k in data]):
		return data
	else:
		for dkey in data:
			if isinstance(data.get(dkey), dict):
				return find_deepest(data.get(dkey))
			else:
				continue


if __name__ == "__main__":
	
	# ss, sdf = get_gsheet(spreadsheet_name="1_Hg3se2g1F7wYjnuRznWUKmGhkI4WXGIZajBIJGQd3Q", sheet_id=169118404)
	ss = get_gsheet(spreadsheet_name="1_Hg3se2g1F7wYjnuRznWUKmGhkI4WXGIZajBIJGQd3Q", sheet_id=169118404)
	df = pd.DataFrame(ss.get_all_records())
	# sheet_to_df
	# import gspread_pandas as gsp
	print(f"df: {df}")
