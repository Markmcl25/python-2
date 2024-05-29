import gspread
from google.oauth2.service_account import Credentials

# Define the scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from the JSON key file
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Authorize the client
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the Google Sheet by name
SHEET = GSPREAD_CLIENT.open('python-2')

# Access the first worksheet (sheet 1)
worksheet = SHEET.get_worksheet(0)

# Function to relay text data back to the sheet
def relay_data_to_sheet(name, email, message):
    """
    Appends a row with the given name, email, and message to the Google Sheet.

    Parameters:
    name (str): The name to add.
    email (str): The email to add.
    message (str): The message to add.
    """
    worksheet.append_row([name, email, message])

# Example usage
text_to_relay = "This is a test message to be relayed back to the Google Sheet."
relay_text_to_sheet(text_to_relay)
print("Text relayed successfully.")
