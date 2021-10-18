import sys
import datetime

if len(sys.argv)<3:
    print("Missing param. You should enter two dates. One date with format dd/mm/yyyy and a numeric param for number of days")
    sys.exit(0)

strDateStart = sys.argv[1]
_days = sys.argv[2]

date_1 = datetime.datetime.strptime(strDateStart, "%d/%m/%Y")
end_date = date_1 + datetime.timedelta(days=int(_days))
print(end_date.strftime("%d/%m/%Y"))