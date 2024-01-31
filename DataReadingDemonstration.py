
import random

def ReadFromFile(fileName) :
    with open(fileName, 'r') as file:
        data = file.read()
        return data
    

def WritetoFile(fileNameWrite): 
    numberData = 6

    largeDataSet = []

    for _ in range(numberData): 

        LotteryLettering = ["A", "B", "C", "D", "E", "F"]

        Shufflingletterorder = random.sample(LotteryLettering, 1)

        aRandomNumber = random.randint(1, 10)

        largeDataSet.append(aRandomNumber)
    
    with open(fileNameWrite, 'w') as file:
        file.write("The Lottery Numbers are shown as the following:")
        for datapoint in largeDataSet:
            file.write(str(Shufflingletterorder) + str(datapoint))
            if _ == NotImplemented :
                break
            else :
                file.write(",")

def isNumber(theString):
    try:
        float(theString)
        return True
    except ValueError:
        return False

theFileName = "Example.txt"

WritetoFile(theFileName)

dataRead = ReadFromFile(theFileName)

print(dataRead)

# if dataRead is not None:
#     for amount in dataRead.split(","):
#         if isNumber(amount):
#             print(f"${int(amount):,.2f}")