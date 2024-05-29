# Google Sheets Command-Line Data Manager

## Project Description

The Google Sheets Command-Line Data Manager is a simple yet powerful application designed to help users manage data in a Google Sheet through a command-line interface (CLI). This project leverages Python and the `gspread` library to interact with Google Sheets, making it easy to add and view data without needing to open a web browser.

### Key Features:
- **Add Data**: Users can input their name, email, and a message, which will then be appended as a new row in the Google Sheet.
- **View Data**: Users can view all existing entries in the Google Sheet, displayed directly in the terminal.

This project is particularly useful for small teams or individuals who need to collect and review data in a structured format but prefer the simplicity and speed of a command-line tool. It can be deployed locally or on cloud platforms like Heroku, making it accessible from anywhere with internet access.

### Use Cases:
- **Event Registrations**: Collect names, emails, and messages from participants.
- **Feedback Collection**: Gather feedback from users or customers in a centralized sheet.
- **Data Logging**: Maintain a log of entries for various purposes such as meeting notes, daily logs, or inventory records.

## Features

- **Add Data**: Users can add new entries with their name, email, and a message.
- **View Data**: Users can view all existing entries in the Google Sheet.

## Requirements

- Python 3.x
- `gspread` library
- `google-auth` library

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/google-sheets-cli-manager.git
   cd google-sheets-cli-manager
