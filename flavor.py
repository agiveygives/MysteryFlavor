import gspread
from random import randint
from datetime import date
from oauth2client.service_account import ServiceAccountCredentials

flavorsURL = 'https://docs.google.com/spreadsheets/d/1nvpNqvJfktkUmWIQ2nla3uZEPts1yzjFizH2xbBEQz8/edit#gid=0'
usedFlavorsURL = 'https://docs.google.com/spreadsheets/d/1nQQpdqnTYwJRIcUH8-Lb_GdHa3K9ju3KDYgGqDCGBiI/edit#gid=0'

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Flavors-690a714b2399.json', scope)

workspace = gspread.authorize(credentials)
flavors = workspace.open_by_url(flavorsURL).sheet1.col_values(1)
usedFlavors = workspace.open_by_url(usedFlavorsURL).sheet1

flavorOfTheFortnite = flavors[randint(0, len(flavors) - 1)]

# add to usedFlavors and remove from flavors
def commitFlavor():
    newRow = len(usedFlavors.col_values(1)) + 1
    usedFlavors.update_cell(newRow, 1, str(date.today()))
    usedFlavors.update_cell(newRow, 2, flavorOfTheFortnite)

def main():
    commit = input(f'{flavorOfTheFortnite} : Is this that good good? (Y/N) ')
    if commit.upper() == 'Y':
        commitFlavor()
    else:
        print(f'{flavorOfTheFortnite} was not writen to the usedFlavors sheet.')

if __name__ == "__main__":
    main()