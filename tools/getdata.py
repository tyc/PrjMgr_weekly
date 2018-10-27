import gspread
import os
import sys
import fileinput
from oauth2client.service_account import ServiceAccountCredentials
from shutil import copyfile
from argparse import ArgumentParser

parser = ArgumentParser()

# parse the command line to get the 
parser.add_argument("-t", "--template", default="template.md", help="specifies the template, defaults to use template.md")
parser.add_argument("outfile", help="specifies the filenaem of the output file")
args = parser.parse_args()

print ("Using template file " + args.template)
print ("Results with merged data is written to " + args.outfile)

# Read in the file
with open(args.template, 'r') as file :
  filedata = file.read()


# lets get the data
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('prjmgr-weekly1-b01f85eb9ee8.json', scope)

gc = gspread.authorize(credentials)

wks1 = gc.open('Saved links for PrjMgr_Weekly').worksheet("Post builder")


# Replace the target string
print "Merging Post 1"
filedata = filedata.replace('%%_A1_POST_CATEGORY_%%', wks1.acell('b2').value)
filedata = filedata.replace('%%_A1_POST_LINK_%%', wks1.acell('b4').value)
filedata = filedata.replace('%%_A1_POST_TITLE_%%', wks1.acell('b3').value)
filedata = filedata.replace('%%_A1_POST_SUMMARY_%%', wks1.acell('b6').value)
filedata = filedata.replace('%%_A1_POST_READING_TIME_%%', wks1.acell('b7').value)
filedata = filedata.replace('%%_A1_POST_TWITTER_SHARE_%%', wks1.acell('b10').value)

print "Merging Post 2"
filedata = filedata.replace('%%_A2_POST_CATEGORY_%%', wks1.acell('b14').value)
filedata = filedata.replace('%%_A2_POST_LINK_%%', wks1.acell('b16').value)
filedata = filedata.replace('%%_A2_POST_TITLE_%%', wks1.acell('b15').value)
filedata = filedata.replace('%%_A2_POST_SUMMARY_%%', wks1.acell('b18').value)
filedata = filedata.replace('%%_A2_POST_READING_TIME_%%', wks1.acell('b19').value)
filedata = filedata.replace('%%_A2_POST_TWITTER_SHARE_%%', wks1.acell('b22').value)

print "Merging Post 3"
filedata = filedata.replace('%%_A3_POST_CATEGORY_%%', wks1.acell('b26').value)
filedata = filedata.replace('%%_A3_POST_LINK_%%', wks1.acell('b28').value)
filedata = filedata.replace('%%_A3_POST_TITLE_%%', wks1.acell('b27').value)
filedata = filedata.replace('%%_A3_POST_SUMMARY_%%', wks1.acell('b30').value)
filedata = filedata.replace('%%_A3_POST_READING_TIME_%%', wks1.acell('b31').value)
filedata = filedata.replace('%%_A3_POST_TWITTER_SHARE_%%', wks1.acell('b34').value)

print "Merging Post 4"
filedata = filedata.replace('%%_A4_POST_CATEGORY_%%', wks1.acell('b38').value)
filedata = filedata.replace('%%_A4_POST_LINK_%%', wks1.acell('b40').value)
filedata = filedata.replace('%%_A4_POST_TITLE_%%', wks1.acell('b39').value)
filedata = filedata.replace('%%_A4_POST_SUMMARY_%%', wks1.acell('b42').value)
filedata = filedata.replace('%%_A4_POST_READING_TIME_%%', wks1.acell('b43').value)
filedata = filedata.replace('%%_A4_POST_TWITTER_SHARE_%%', wks1.acell('b46').value)


# Write the file out again
with open(args.outfile, 'w') as file:
  file.write(filedata)

