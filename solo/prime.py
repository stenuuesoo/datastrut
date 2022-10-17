import time

numberList = list(range(1, 100))
newPrimeList = []
controlPrimeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
notPrimes = []

def checkPrime(numberList):
    if numberList:
        if numberList[0] > 1:
            if primeFactor(numberList[0]):
                notPrimes.append(numberList[0])
            if not primeFactor(numberList[0]): 
                newPrimeList.append(numberList[0])
        checkPrime(numberList[1:])  

def primeFactor(primeNumberCandidate):
    for factorNumber in range(2, primeNumberCandidate):
        if primeNumberCandidate % factorNumber == 0:
            return True

def controlList(newPrimeList):
    return newPrimeList == controlPrimeList
        
def printNumbers():
    print('\nPrime Numbers - {}'.format(newPrimeList))       
    print('Not Prime Numbers - {}'.format(notPrimes))
        
def runCode():
    st = time.time()
    checkPrime(numberList)
    printNumbers()
    et = time.time()
    return (et - st) * 1000

def main():
    print('\nExecution time: {} seconds. Prime Numbers - {} '.format(runCode(),controlList(newPrimeList)))
    
if __name__ == "__main__":
    main()