from google.colab import auth
auth.authenticate_user()

import gspread
from google.auth import default
creds, _ = default()

gc = gspread.authorize(creds);

spreadsheet = gc.open('ACME-HappinessSurvey2020')
