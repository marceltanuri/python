import datetime
import sys

if len(sys.argv)<3:
    print("Missing param. You should enter two dates with format dd/mm/yyyy")
    sys.exit(0)

strDateStart = sys.argv[1]
strDateEnd = sys.argv[2]

dateStart = datetime.datetime.strptime(strDateStart, "%d/%m/%Y")
dateEnd = datetime.datetime.strptime(strDateEnd, "%d/%m/%Y")
delta = dateEnd - dateStart
print(delta.days)