import sys
import datetime

# Return estimated birth dates based on gestational weeks and date of the last medical exam
# Param 1: Date of medical exam
# Param 2: Number of gestational weeks in the date of the medical exam

if len(sys.argv)<3:
    print("Missing param. You should enter two dates. One date with format dd/mm/yyyy and a numeric param for number of weeks")
    sys.exit(0)

medicalExam_examDate = datetime.datetime.strptime(sys.argv[1], "%d/%m/%Y")
medicalExam_gestationWeeks = sys.argv[2]

readyToBorn = 38 #weeks
maxTimeToBorn = 42 #weeks
threshold = (maxTimeToBorn - readyToBorn) #weeks

ramainingWeeks = readyToBorn - int(medicalExam_gestationWeeks)

for i in range(threshold):
    estimatedBirthDate = medicalExam_examDate + datetime.timedelta(weeks=int(ramainingWeeks) + i)
    print("With", readyToBorn + i, "weeks:", estimatedBirthDate.strftime("%d/%m/%Y"))