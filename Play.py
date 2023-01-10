def main():
    student_grades = []
    length = int(input("Enter no.of.students: "))
    for i in range(length):
        name = input("Enter student name:")
        score = float(input("Enter marks:"))
        student_grades.append([name,score])
    print(student_grades)

    sort_grad = [student_grades[i][1] for i in range(len(student_grades)) ]
    sort_grad.sort()
    second_lowest = []
if __name__ == '__main__':
    main()
