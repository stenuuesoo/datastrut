# find percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks:
        avg = sum(student_marks[query_name])/len(student_marks[query_name])
        print("%.2f" % avg)
        
    # Test Data
    # Krishna 67 68 69
    # Arjun 70 98 63  
    # Malika 52 56 60