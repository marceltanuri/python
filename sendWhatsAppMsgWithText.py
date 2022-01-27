import os
import sys
import re

WHATSAPP_API = "https://api.whatsapp.com/send"

def getPhoneFromParam():
    # removes any non-numeric character from param
    return re.sub("[^0-9]", "", sys.argv[1])


if(len(sys.argv) < 2):
    exit()

os.system('start chrome ' + '"' + WHATSAPP_API+"?phone="+sys.argv[1]+"&text="+sys.argv[2]+'"')
