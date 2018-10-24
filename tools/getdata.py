import gspread
from oauth2client.service_account import ServiceAccountCredentials
from shutil import copyfile
from argparse import ArgumentParser

parser = ArgumentParser()

# parse the command line to get the 
parser.add_argument("-t", "--template", default="template.md", help="specifies the template, defaults to use template.md")
parser.add_argument("outfile", help="specifies the filenaem of the output file")
args = parser.parse_args()

print (args.template)
print (args.outfile)

copyfile("template.md","fatdog.txt")

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('prjmgr-weekly1-b01f85eb9ee8.json', scope)

gc = gspread.authorize(credentials)

wks1 = gc.open('Saved links for PrjMgr_Weekly').worksheet("Post builder")

print(wks1.acell('b2').value)
print(wks1.acell('b3').value)
print(wks1.acell('b4').value)

