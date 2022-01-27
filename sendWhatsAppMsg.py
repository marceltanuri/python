import os
import re
import sys

WHATSAPP_API="https://api.whatsapp.com/send"

def getPhoneFromParam():
    phone=""
    for item in sys.argv[1:]:
        phone += re.sub("[^0-9]", "", item) # removes any non-numeric character from param
    return phone

if(len(sys.argv)<2):
    exit()

os.system('start chrome ' + WHATSAPP_API+"?phone="+getPhoneFromParam())
