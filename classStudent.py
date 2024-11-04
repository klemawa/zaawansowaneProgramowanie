class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average >= 5

student1 = Student("Klema", [6,5,6,6,6,5,6,6,5,6,6,6,6,6,6,5,5,5,6,5])
student2 = Student("Ola", [3,3,2,2,2,2,2,2,2,3,2,3,2,3,2,2,2,2,4,2])

print(f"{student1.name}, {student1.is_passed()}")
print(f"{student2.name}, {student2.is_passed()}")