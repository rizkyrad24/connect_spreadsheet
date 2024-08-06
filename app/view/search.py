from fastapi import HTTPException, status
import os

from apiclient import discovery
from google.oauth2 import service_account

class ConnectSpreadsheet:
    def search(self, sheet, company):
        try:
            sheet_name = sheet
            scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
            secret_file = os.path.join(os.getcwd(), 'credentials.json')

            spreadsheet_id = '187-gHKnBh4IaKYbuYO56-dOi0kExPYByuWsLyQWmZps'

            credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
            service = discovery.build('sheets', 'v4', credentials=credentials)
            
            sheet = service.spreadsheets()

            bot_id = None
            jml_klik = None
            jml_user = None

            rows = sheet.values().get(spreadsheetId=spreadsheet_id, range=f"{sheet_name}!A2:D12").execute()
            values = rows.get("values", [])
            for value in values:
                if value[0] == company:
                    bot_id = value[1]
                    jml_klik = value[2]
                    jml_user = value[3]
            
            if bot_id and jml_klik and jml_user:
                return {
                    "message": "Data ditemukan",
                    "company": company,
                    "bot_id": bot_id,
                    "jml_klik": jml_klik,
                    "jml_user": jml_user
                }
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Data Tidak Ditemukan"
                )

        except OSError as e:
            print(e)
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Data Tidak Ditemukan"
                )
