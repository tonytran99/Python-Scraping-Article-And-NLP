import csv
import math

reader = csv.DictReader(open('frequencyUpper.csv'))

for line in reader:
    lenUpper = len(line)
    arrayKeyDict = list(line)
    break

dictFrequencyUpper = []
with open("frequencyUpper.csv") as f:
    records = csv.DictReader(f)
    for row in records:
        dictFrequencyUpper.append(row)


def checkRelationship(index1, index2):
    sumSquare1 = 0
    sumSquare2 = 0
    sumRelative = 0
    for i in range(2000):
        sumSquare1 += int(dictFrequencyUpper[i][arrayKeyDict[index1]]) ** 2
        sumSquare2 += int(dictFrequencyUpper[i][arrayKeyDict[index2]]) ** 2
        sumRelative += int(dictFrequencyUpper[i][arrayKeyDict[index1]]) * int(
            dictFrequencyUpper[i][arrayKeyDict[index2]])

    checkRelative = sumRelative / math.sqrt(sumSquare1 * sumSquare2)

    if checkRelative > 0.5:
        return True
    return False


dictIndex1 = {}
dictIndex2 = {}
index = 0
for index1 in range(1, 300):
    for index2 in range(index1 + 1, 300):
        dictIndex1[index] = index1
        dictIndex2[index] = index2
        index += 1
print(len(dictIndex1))


dictCoupleUpperRelative = []
csvColumns = {'character1', 'character2'}

for i in range(len(dictIndex1)):
    if checkRelationship(dictIndex1[i], dictIndex2[i]):
        rowCoupleUpperRelative = {'character1': arrayKeyDict[dictIndex1[i]], 'character2': arrayKeyDict[dictIndex2[i]]}
        dictCoupleUpperRelative.append(rowCoupleUpperRelative)

try:
    with open('coupleUpperRelationship.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csvColumns)
        writer.writeheader()
        for data in dictCoupleUpperRelative:
            writer.writerow(data)
except IOError:
    print("I/O error")
