import sys
import datetime

if len(sys.argv)<3:
    print("Missing param. You should enter two dates. One date with format dd/mm/yyyy and a numeric param for number of weeks")
    sys.exit(0)

strDateStart = sys.argv[1]
_weeks = sys.argv[2]

date_1 = datetime.datetime.strptime(strDateStart, "%d/%m/%Y")

end_date = date_1 + datetime.timedelta(weeks=int(_weeks))
print(end_date.strftime("%d/%m/%Y"))