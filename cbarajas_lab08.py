class Student:
	"""Used to create the student class	"""

	def __init__(self, lastname, firstname, idnum):
		"""(Student, str, str, int) -> None

		Used for intializing the Student object.

		>>> Student('Fluffykins', 'Sir', 123456789)
		Student('Fluffykins', 'Sir', 123456789)
		"""
		self.firstname = firstname.strip()
		self.lastname = lastname.strip()
		self.idnum = idnum
	
	def __str__(self):
		"""(Student) -> str

		Returns the Student object's ID, last name, first name in the format
		lastname, firstname: ID.

		>>> str(Student('Fluffykins', 'Sir', 123456789))
		'Fluffykins, Sir: 123456789'
		"""
		return '{}, {}: {}'.format(self.lastname, self.firstname, self.idnum)
	
	def __repr__(self):
		"""(Student) -> str

		Returns the string of the command required to instaniate the Student
		object.

		>>> repr(Student('Fluffykins', 'Sir', 123456789))
		"Student('Fluffykins', 'Sir', 123456789)"
		"""
		return "Student('{}', '{}', {})".format(self.lastname, self.firstname, self.idnum)

	def __eq__(self, student2):
		"""(Student, Student) -> bool

		Compares two Student objects and lets you know if they are equal.
		StudentObject1 == StudentObject2


		>>> Student('Fluffykins', 'Sir', 123456789) == Student('Fluffykins', 'Sir', 123456789)
		True
		
		>>> Student('Fluffykins', 'Sir', 123456789) == Student('Fluffykin', 'Sir', 12345679)
		False
		
		>>> Student('Fluffykins', 'Sir', 123456789) == Student('Fluffykins', 'Sr', 1234589)
		False
		
		>>> Student('Fluffykins', 'Sir', 123456789) == Student('Fluffykins', 'Sir', 125678)
		False
		"""
		return self.idnum == student2.idnum

	def __ne__(self, student2):
		"""(Student, Student) -> bool

		Says whether or not two Student
		StudentObject1 != StudentObject2

		>>> Student('A', 'A', 0) != Student('A', 'B', 0)
		True
		"""
		return (self.idnum, self.lastname.lower(), self.firstname.lower()) != (
			student2.idnum, student2.lastname.lower(), student2.firstname.lower())

	def __gt__(self, student2):
		"""(Student, Student) -> bool

		Compared two students and determines if self is greater than student2
		StudentObject1 > StudentObject2

		>>> Student('Aaa', 'Aaa', 123) > Student('Aaa', 'Aaa', 123)
		False

		>>> Student('Aaa', 'Aaa', 123) > Student('Baa', 'Aaa', 123)
		False

		>>> Student('Aaa', 'Zaa', 123) > Student('Aaa', 'Aaa', 123)
		True
		"""
		if self.lastname.lower() > student2.lastname.lower():
			return True
		elif self.lastname.lower() == student2.lastname.lower():
			if self.firstname.lower() > student2.firstname.lower():
				return True
			elif self.firstname.lower() == student2.firstname.lower():
				if self.idnum > student2.idnum:
					return True
		return False

	def __ge__(self, student2):
		"""(Student, Student) -> bool
		Determines if self is greater than or equal to student2
		StudentObject1 >= StudentObject2

		>>> Student('Fluffykins', 'Sir', 123456789) >= Student('Fluffykins', 'Sir', 123456789)
		True
		
		>>> Student('Aaa', 'Baa', 123456789) >= Student('Aaa', 'Aaa', 1234569)
		True
		
		>>> Student('Fluff', 'Sir', 123456789) >= Student('Fluffykins', 'Sir', 1234)
		False
		
		>>> Student('Fluffykins', 'Sir', 123456789) >= Student('Fluffykins', 'Sir', 45678)
		True
		"""
		if self == student2 or self > student2:
			return True
		return False

	def __lt__(self, student2):
		"""(Student, Student) -> bool

		Determines whether Self is less than student2
		StudentObject1 < StudentObject2

		>>> Student('Aaa', 'Aaa', 1232) < Student('Aaa', 'Aaa', 123)
		False

		>>> Student('Aaa', 'Aaa', 1230) < Student('Baa', 'Aaa', 123)
		True

		>>> Student('Aaa', 'Zaa', 1234) < Student('Aaa', 'Aaa', 123)
		False
		"""
		return not (self == student2 or self > student2)
		# if not greater than or equal to than must be false

	def __le__(self, student2):
		"""(Student, Student) -> bool

		Determines whether or not Self is less than or equal to student2
		StudentObject1 <= StudentObject2

		>>> Student('Aaa', 'Aaa', 123) <= Student('Aaa', 'Aaa', 123)
		True

		>>> Student('Aaa', 'Aaa', 1231) <= Student('Baa', 'Aaa', 123)
		True

		>>> Student('Aaa', 'Zaa', 1223) <= Student('Aaa', 'Aaa', 123)
		False
		"""
		return self == student2 or self < student2



class HonorStudent(Student):
	"""Creates the HonorStudent object"""

	def __init_(self, lastname, firstname, idnum, gpa):
		"""(Student, str, str, int, float) -> None

		Used for intializing the HonorStudent object.
		"""
		super().__init__(lastname, firstname, idnum)
		self.GPA = gpa


def student_sort(students):
	"""(list of Student objects) -> list

	Uses merge sort to sort a list of Student objects.
	"""
	workspace = []
	for item in students:
		workspace.append([item])
	pos = 0
	while pos + 1 < len(workspace):
		workspace.append(
			catinate(workspace[pos], workspace[pos + 1]))
		pos += 1
	return workspace[-1]


def catinate(list1, list2):
	"""(list, list) -> list

	concatinates and sorts list1 and list2 into finalist"""
	index1 = 0
	index2 = 0
	finalist = []
	while index1 < len(list1) and index2 < len(list2):
		if list1[index1] < list2[index2]:
			finalist.append(list1[index1])
			index1 += 1
		else:
			finalist.append(list2[index2])
			index2 += 1
	finalist.extend(list1)
	finalist.extend(list2)
	return finalist


def student_search(students, item):
	"""(list) -> int

	Returns the index of the item in list students. If item is not in list
	then returns -1.
	"""
	start = 0
	end = len(students) - 1
	while start < end:
		middle  = end // 2
		if students[middle] == item:
			return middle
		elif students[middle] < item:
			start = middle + 1
		else:
			end = middle - 1
	return -1


if __name__ == '__main__':
	import doctest
	doctest.testmod()