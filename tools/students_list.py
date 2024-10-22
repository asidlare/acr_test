import unicodedata
from dataclasses import dataclass
from functools import total_ordering


'''
I used a method with my own comparison because whatever else I'll use instead
(lambda, itemgetter, attrgetter), I'll still have problem with that I need asc and desc
sorting.
Regarding locale, I simple helper based on unicodedata.
Each student object is compared once (objects are compared) and I use sorting in place,
so regarding efficiency, I have no idea now what else I can do.
'''


@total_ordering
@dataclass
class Student:
    grade: int
    first_name: str
    last_name: str

    @staticmethod
    def _transliterate(text: str) -> str:
        return (
            unicodedata.normalize("NFD", text)
            .encode('ascii', errors='ignore')
            .decode('ascii', errors='ignore')
        )

    def __gt__(self, other):
        grade_cond = self.grade > other.grade
        last_name_cond = self._transliterate(self.last_name) > self._transliterate(other.last_name)
        first_name_cond = self._transliterate(self.first_name) < self._transliterate(other.first_name)
        return grade_cond and last_name_cond and first_name_cond

    def __repr__(self):
        return f"Student(grade={self.grade}, first_name={self.first_name}, last_name={self.last_name})"


def sorted_students(students: list[Student]) -> list[Student]:
    students.sort()
    return students


if __name__ == '__main__':
    students = []
    students.append(Student(60, 'Włodzimierz', 'Kowalski'))
    students.append(Student(60, 'Wlodzimierz', 'Kowalski'))
    students.append(Student(70, 'Jan', 'Kowalski'))
    students.append(Student(70, 'Adam', 'Kowalski'))
    students.append(Student(70, 'Ądam', 'Kowalski'))
    students.append(Student(70, 'Jan', 'Nowak'))
    students.append(Student(70, 'Jan', 'Żak'))
    print(sorted_students(students))
