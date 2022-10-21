# Initialize your list and read in the value of followed by lines of commands where each command will be of the  types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

test1 = [12, "insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9", "append 1", "sort", "print", "pop", "reverse", "print"]

commands = []
arr = []
splitted = []

def insert_i_at_e(i, e):
    arr.insert(i, e)

def append(i):
    arr.append(i)
    
def remove(i):
    if(i) in arr:
        arr.remove(i)

def main(N):
     while N > 0:
         newCommand = input()
         newCommand = newCommand.split()
         if newCommand[0] in commands:
             print("Headroll")
            
if __name__ == '__main__':
    N = int(input())
    main(N)