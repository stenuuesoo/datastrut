import time
st = time.time()

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
saved = []

def fi(list, el):
    if el not in saved:
        print(el, end=" ")
        saved.append(el)
        for el in list:
            fi(list, el)

def lo(saved, el):
    for el in reversed(saved):
        print(el, end=" ")
        saved.pop()
        lo(saved, el - 1)

print("\nFirst in: ")        
fi(list, list[0])
print("\nLast out: ")
lo(saved, saved[0])

et = time.time()
elapsed_time = (et - st) * 1000
print('\nExecution time:', elapsed_time, 'seconds')
