import os
import re
import sys

page="https://www.google.com"

if len(sys.argv)<2:
    print("Missing param. You should enter a page")
    sys.exit(0)

page = sys.argv[1]


os.system('start chrome ' + page)
