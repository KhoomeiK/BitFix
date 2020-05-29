from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import csv
# from database import parse
# from googleapiclient.http import MediaIoBaseDownload
# import io
# from httplib2 import http
# from 

# If modifying these scopes, delete the file token_sheets.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
# SCOPES = ['https://www.googleapis.com/auth/drive',
#           'https://www.googleapis.com/auth/drive.readonly']

# The ID and name of the spreadsheet.
SPREADSHEET_ID = '1AC6n9a8mnoAD67URnM7ZjCzEoI0p3odtdUhnOmynGbw'
SHEET_NAME = 'Form Responses 1'

def get_sheet():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token_sheets.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token_sheets.pickle'):
        with open('token_sheets.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token_sheets.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # file_id = '1sT720pjfbOsJm9fBt1XWJM8e5C_dg6_UGAZg2heTbOw'
    # request = service.files().get(fileId=file_id, mimeType='application/pdf')
    # with open('myamazing.pdf', 'w') as f:
    #     f.write(request.get(values))

    # fh = io.FileIO('test_responses', 'w')
    # downloader = MediaIoBaseDownload(fh, request)
    # done = False
    # while done is False:
    #     status, done = downloader.next_chunk()
    #     print ("Download %d%%." % int(status.progress() * 100))
        # print(status)



    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=SHEET_NAME).execute()
    
    output_file = 'test_responses.csv'
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        with open(output_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(values)
        f.close()
        # parse('test_responses.csv')


        # writeToFile(values)
        # print('Name, Major:')
        # print(values[1])
        # for row in values:
        #     # Print columns A and E, which correspond to indices 0 and 4.
        #     print('%s, %s' % (row[0], row[4]))


# def writeToFile(values):
#     file = open("responses2.csv", "w")
#     for line in values:
#         for element in line[:-1]:
#             file.write(element + ", ")
#         file.write(line[-1])
#         file.write("\n")
#     file.close()


# if __name__ == '__main__':
#     main()
