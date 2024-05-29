import gspread
from google.oauth2.service_account import credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python-2')

in_going = SHEET.worksheet('input')

def relay_text_to_sheet(text):
    """
    Appends a row with the given text to the Google Sheet.

    Parameters:
    text (str): The text to relay back to the sheet.
    """
    worksheet.append_row([text])