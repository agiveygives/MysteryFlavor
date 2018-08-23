# Mystery Flavored

## First time running

### Create google oauth2 json
1. Navigate to the [Google API Dashboard](https://console.developers.google.com/apis/)
2. Click 'Enable APIs and Services'
3. Search for Sheets and enable it.
4. Once enabled, you should get redirected to the dashboard. If you aren't, press the 'Manage' button to naviagate there.
5. From the dashboard, click 'Create Credentials'
6. Select: Google Sheets API, Other UI, and Application Data
7. Enter your service account name.
8. Select the role as 'Owner'.
9. Select the JSON key type.
10. Once the key is created, put it into the MysteryFlavor directory.
--

Must have [python 3](https://www.python.org/downloads/) installed with pip commands.

```
pip install gspread
pip install oauth2client
pip install pygame
```

## How to use
1. run ```python mystery.py``` (you may have to do ```python3 mystery.py``` depending on how you installed)
2. The window may not open in focus, click into the window
3. Press Enter to commit the new flavor or press Escape to quit without commiting

Flavors are pulled from [this spread sheet](https://docs.google.com/spreadsheets/d/1nvpNqvJfktkUmWIQ2nla3uZEPts1yzjFizH2xbBEQz8/edit#gid=0)
Used Flavors are written to [this spread sheet](https://docs.google.com/spreadsheets/d/1nQQpdqnTYwJRIcUH8-Lb_GdHa3K9ju3KDYgGqDCGBiI/edit#gid=0)
