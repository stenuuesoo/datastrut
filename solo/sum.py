
list = list(range(1, 100))

def forsum(list):
    sum = 0
    for i in list:
       sum += i
    return sum

def recsum(list):
        return list[0] + recsum(list[1:]) if list else 0

print("\nTotal of 1 to 100:", forsum(list))
print("\nTotal of 1 to 100:", recsum(list))