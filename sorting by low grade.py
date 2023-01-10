def main():
    student_grades = []
    length = int(input("Enter no.of.students: "))
    for i in range(length):
        name = input("Enter student name:")
        score = float(input("Enter marks:"))
        student_grades.append([name, score])
    sort_grad = sorted(list(set([x[1] for x in student_grades])))
    print(sort_grad)
    x = sort_grad[1]

    low_list = []
    for student in student_grades:
        if x == student[1]:
            low_list.append(student[0])
    print(low_list)

    for student in sorted(low_list):
        print("The second lowest score belonged to ", student)


if __name__ == '__main__':
    main()
