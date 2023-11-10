import gspread

class WorksheetDictWriter:
    """
    Something like a `csv.DictWriter`, except for a `gspread.Worksheet`
    """

    def __init__(self, worksheet: gspread.Worksheet, fieldnames: list[str], column="A"):
        self.fieldnames = fieldnames
        self.worksheet = worksheet
        self.column = column
        self.num_filled_rows = len(self.worksheet.get_all_values())
        self.current_row = 1 + self.num_filled_rows

    def writeheader(self):
        self.writerow(dict(zip(self.fieldnames, self.fieldnames)))

    def writerow(self, row: dict[str, str]):
        to_write = []
        for name in self.fieldnames:
            to_write.append(row.get(name, ""))
        self.worksheet.update(f"{self.column}{self.current_row}", [to_write])
        # (self.sheet_id)["Tools"].update(f"{self.column}{self.current_row}", [to_write])
        self.current_row += 1

    def writerows(self, rows: list[dict[str, str]]):
        for row in rows:
            self.writerow(row)
