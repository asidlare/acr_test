from tools.students_list import sorted_students, Student


def test_students_list():
    students = []
    students.append(Student(60, 'Włodzimierz', 'Kowalski'))
    students.append(Student(60, 'Wlodzimierz', 'Kowalski'))
    students.append(Student(70, 'Jan', 'Kowalski'))
    students.append(Student(70, 'Adam', 'Kowalski'))
    students.append(Student(70, 'Ądam', 'Kowalski'))
    students.append(Student(70, 'Jan', 'Nowak'))
    students.append(Student(70, 'Jan', 'Żak'))

    res = sorted_students(students)

    assert str(res[0]) == 'Student(grade=70, first_name=Jan, last_name=Żak)'
    assert str(res[1]) == 'Student(grade=70, first_name=Jan, last_name=Nowak)'
    assert str(res[2]) == 'Student(grade=70, first_name=Ądam, last_name=Kowalski)'
    assert str(res[3]) == 'Student(grade=70, first_name=Adam, last_name=Kowalski)'
    assert str(res[4]) == 'Student(grade=70, first_name=Jan, last_name=Kowalski)'
    assert str(res[5]) == 'Student(grade=60, first_name=Wlodzimierz, last_name=Kowalski)'
    assert str(res[6]) == 'Student(grade=60, first_name=Włodzimierz, last_name=Kowalski)'
