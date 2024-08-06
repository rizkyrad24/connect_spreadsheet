## How To Install:
1. Clone or download this repository
2. Create virtual environment. Run this command in the terminal
     python -m venv env
3. Install requirements.txt
    pip install -r requirements.txt
4. Put credentials.json in main directory. You can read the instruction bellow to create credentials.json
5. run the server. run this command in the terminal
    uvicorn main:app --port 8000 --reload

** dont use --reload for production.

## How to get cretentials.json
1. open https://console.developers.google.com/
2. create new project
3. Enable APIs and services for Google Drive API and Google Sheets API
4. Create New Credentials. Choose Service Account
5. Then create json key, click your new credential, choose KEYS, click add key and Create new key. Choose json and the json key will be downloaded. Change the json key name to be credentials.json and put it in the main directory.

## Spreadsheet
This code point to the spreadsheet in https://docs.google.com/spreadsheets/d/187-gHKnBh4IaKYbuYO56-dOi0kExPYByuWsLyQWmZps/edit?usp=sharing
