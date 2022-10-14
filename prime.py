import time

numberList = list(range(1, 100))
newPrimeList = []
controlPrimeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def checkPrime(numberList):
    if numberList:
        if numberList[0] > 1:
            if not primeFactor(numberList[0]): 
                newPrimeList.append(numberList[0])
        checkPrime(numberList[1:])  

def primeFactor(primeNumberCandidate):
    for factorNumber in range(2, primeNumberCandidate):
        if primeNumberCandidate % factorNumber == 0:
            return True

def controlList(newPrimeList):
    return newPrimeList == controlPrimeList

def runCode():
    st = time.time()
    checkPrime(numberList)
    et = time.time()
    return (et - st) * 1000

def main():
    print('\nExecution time: {} seconds. Prime Numbers - {} '.format(runCode(),controlList(newPrimeList)))
    for primes in newPrimeList:
        print(primes, end=' ')
    
if __name__ == "__main__":
    main()