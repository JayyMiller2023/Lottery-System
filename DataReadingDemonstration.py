
import random

def ReadFromFile(fileName) :
    with open(fileName, 'r') as file:
        data = file.read()
        return data
    

def WritetoFile(fileNameWrite): 
    numberData = 6

    largeDataSet = []

    for _ in range(numberData): 

        LotteryLettering = random.choice["A", "B", "C", "D", "E", "F"]

        aRandomNumber = random.randint(1, 10)

        largeDataSet.append(LotteryLettering + aRandomNumber)
    
    with open(fileNameWrite, 'w') as file:
        file.write("The Lottery Numbers are shown as the following:")
        for datapoint in largeDataSet:
            file.write(str(datapoint))
            if datapoint == NotImplemented :
                return False
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