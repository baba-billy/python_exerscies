class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age


class Student(Person):

	def __init__(self, name, age, grade, subjects = []):
		super().__init__(name, age)
		self.grade = grade
		self.subjects = subjects

	def enroll_subject(self, subject):
		self.subjects.append(subject)

class Teacher(Person):

	def __init__(self, name, age, subject):
		super().__init__(name, age)
		self.subject = subject

	def teach(self, student):
		print(f"{self.name} teaches, {self.subject} to {student.name}")


class School:

	def __init__(self, name, students = [], teachers = []):
		self.name = name
		self.students = students
		self.teachers = teachers

	def add_student(self, student):
		self.students.append(student)

	def add_teacher(self, teacher):
		self.teachers.append(teacher)

	def show_all_students(self):
		for student in self.students:
			print(student.name)
	
	def show_all_teachers(self):
		for teacher in self.teachers:
			print(teacher.name)


student1 = Student("rico", 19, 4, ["English", "Yoruba"])
student2 = Student("jane", 15, 2, ["Science", "Economics"])

teacher1 = Teacher("Dele", 25, "Science")
teacher2 = Teacher("Faruq", 30, "English")

teacher1.teach(student1)

school = School("IESHS", [student1, student2], [teacher1, teacher2])
school.show_all_students()
school.show_all_teachers()
print(student1.grade)