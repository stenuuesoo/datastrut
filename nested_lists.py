# Given the names and grades for each student in a class of  students, store them in a nested list and 
# print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and 
# print each name on a new line.


students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
students2 = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]
#students = []
similarGrades = []

if __name__ == '__main__':
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students.append([name, score])
    
    students.sort(key=lambda x: x[1])
    minvalue = min(students, key=lambda x: x[1])
    
    for element in students:
        if element[1] == minvalue[1]:
            students.remove(element)
    
    if students[0][1] == minvalue[1]: students.remove(students[0])
    
    minvalue = min(students, key=lambda x: x[1])
    
    for element in students:
        if element[1] == minvalue[1]:
            similarGrades.append(element)
            
    similarGrades.sort()
    for element in similarGrades: print(element[0])
