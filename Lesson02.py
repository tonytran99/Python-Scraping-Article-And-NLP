import numpy
import re
from nltk.corpus import stopwords
import csv

arrayStopwords = stopwords.words('english')

# Get All Character Article
arrayAllCharacterArticleDuplicate = {}
index = 0
for i in range(1, 2001):
    fileNameArticle = str(i) + '.txt'
    fileArticle = open("file_articles/" + fileNameArticle, "r")
    contentFileArticle = fileArticle.read()
    fileArticle.close()
    arrayCharacterArticle = contentFileArticle.split()
    for characterArticle in arrayCharacterArticle:
        arrayAllCharacterArticleDuplicate[index] = characterArticle
        index += 1

# Delete Duplicate Character In All Character Article
arrayAllCharacterArticleDeleteDuplicate = set(list(arrayAllCharacterArticleDuplicate.values()))
# array to dict
arrayAllCharacterArticle = {}
index = 0
for item in arrayAllCharacterArticleDeleteDuplicate:
    arrayAllCharacterArticle[index] = item
    index += 1

# Get All Upper Character Article
arrayAllUpperCharacterArticle = {}
index = 0
for i in range(1, len(arrayAllCharacterArticle)):
    regexUpperCharacter = "^[A-Z]([A-Z]{0,}[a-z]{0,}){0,}$"
    checkUpperCharacter = re.findall(regexUpperCharacter, arrayAllCharacterArticle[i])
    if (len(checkUpperCharacter) == 1) & (arrayStopwords.count(arrayAllCharacterArticle[i].lower()) == 0):
        arrayAllUpperCharacterArticle[index] = arrayAllCharacterArticle[i]
        index += 1

print(arrayAllUpperCharacterArticle)

# Get frequency save csv file
dictFrequencyUpper = []
csvColumns = numpy.array(["fileName"])
csvColumns = numpy.append(csvColumns, list(arrayAllUpperCharacterArticle.values()), axis=0)
for i in range(1, 2001):
    fileNameArticle = str(i) + '.txt'
    fileArticle = open("file_articles/" + fileNameArticle, "r")
    contentFileArticle = fileArticle.read()
    fileArticle.close()
    arrayCharacterArticle = contentFileArticle.split()
    arrayFrequencyOneFile = numpy.array([fileNameArticle])
    rowArticle = {'fileName': fileNameArticle}
    for j in range(len(arrayAllUpperCharacterArticle)):
        frequencyUppercase = arrayCharacterArticle.count(arrayAllUpperCharacterArticle[j])
        rowArticle[arrayAllUpperCharacterArticle[j]] = frequencyUppercase

    dictFrequencyUpper.append(rowArticle)

try:
    with open('frequencyUpper.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csvColumns)
        writer.writeheader()
        for data in dictFrequencyUpper:
            writer.writerow(data)
except IOError:
    print("I/O error")
