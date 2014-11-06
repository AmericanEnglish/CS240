class Score:
	"""Creates the score class"""

	def __init__(self, points, initials):
		"""(Score, int, str) -> Score

		Used for initializing Score objects. Takes the intials as a str
		and the score would have to be an int.
		"""
		self.points = points
		self.initials = initials.upper()

	def __str__(self):
		"""(Score) -> str

		Returns the string of the score and the initials that are saved
		inside the Score object.

		>>> str(Score(100, 'AAA'))
		'100 AAA'
		
		>>> str(Score(200, 'AAB'))
		'200 AAB'
		"""
		return '{} {}'.format(self.points, self.initials)

	def __repr__(self):
		"""(Score) -> str

		Returns the string of the input needed to generate the score object.

		>>> repr(Score(100, 'AAA'))
		"Score(100, 'AAA')"
		
		>>> repr(Score(200, 'BBB'))
		"Score(200, 'BBB')"
		"""
		return "Score({}, '{}')".format(self.points, self.initials)

	def __lt__(self, obj):
		"""(Score, Score) -> bool

		Determines whether the self is less than the Score obj. Returns
		True if self < obj and false for all other cases of equality.
		Compares points first then compares initials.

		>>> Score(100, 'AAA') < Score(101, 'AAA')
		True

		>>> Score(100, 'AAA') < Score(99, 'AAA')
		False

		>>> Score(100, 'AAA') < Score(100, 'AAB')
		True

		>>> Score(100, 'AAA') < Score(100, 'AAA')
		False
		"""
		return (self.points, self.initials) < (obj.points, obj.initials)

	def __gt__(self, obj):
		"""(Score, Score) -> bool


		Determines if self > obj. First compares score and then compares
		initials. Returning True if self > obj.
		
		>>> Score(100, 'AAA') > Score(101, 'AAA')
		False

		>>> Score(100, 'AAA') > Score(99, 'AAA')
		True

		>>> Score(100, 'AAA') > Score(100, 'AAB')
		False

		>>> Score(100, 'AAA') > Score(100, 'AAA')
		False
		"""
		return (self.points, self.initials) > (obj.points, obj.initials)

	def __eq__(self, obj):
		"""(Score, Score) -> bool

		Determines if self is equal to obj. Meaning that is the initials
		and the score are the same then the statement will return True.
		Al other cases of equality will return false.

		>>> Score(100, 'AAA') == Score(101, 'AAA')
		False

		>>> Score(100, 'AAA') == Score(99, 'AAA')
		False

		>>> Score(100, 'AAA') == Score(100, 'AAB')
		False

		>>> Score(100, 'AAA') == Score(100, 'AAA')
		True
		"""
		return (self.points, self.initials) == (obj.points, obj.initials)

	def __ne__(self, obj):
		"""(Score, Score) -> bool

		Compares two Score objects and then determines if self is not
		equal to obj. If this case is true returns True. All other cases
		will return False.
		
		>>> Score(100, 'AAA') != Score(101, 'AAA')
		True

		>>> Score(100, 'AAA') != Score(99, 'AAA')
		True

		>>> Score(100, 'AAA') != Score(100, 'AAB')
		True

		>>> Score(100, 'AAA') != Score(100, 'AAA')
		False
		"""
		return not self == obj


class DetailedScore(Score):
	"""Creates a detailed score object using things from the Scire class"""

	def __init__(self, points, initials, level):
		"""(Score, int, str, int) -> None

		Used for initializing DetailedScore object.
		"""
		super().__init__(points, initials)
		self.level = level

	def __str__(self):
		"""(DetailedScore) -> str

		Returns the string for the DetailedScore object.

		>>> str(DetailedScore(100, 'AAA', 2))
		'100 AAA 2'
		"""
		#return '{} {}'.format(super().__str__(self), self.level)
		return '{} {} {}'.format(self.score, self.initials, self.level)

	def __repr__(self):
		"""(DetailedScore) -> str

		Returns the string needed to generate the DetailedScore obj.

		>>> repr(DetailedScore(100, 'AAA', 2))
		"DetailedScore(100, 'AAA', 2)"
		"""
		return "DetailedScore({}, '{}', {})".format(self.score, self.initials, self.level)

def sort_scores(listy):
	"""(list of Scores) -> None

	Uses selection sort to sort a list of scores.
	"""
	foddervalue = listy[0]
	fodderindex = 0
	n = 0 #used for tracking sorted portion
	while n < len(listy) - 1:
		for index in range(n + 1, len(listy)):
			if listy[n] > listy [index]:
				listy[n], listy[index] = listy[index], listy[n]
		n += 1


def search_scores(listy, item):
	"""(list of Scores, Score) -> index

	uses a binary search to search a list of scores then returns the index
	if Score is found. If the Score is not found the function will return -1
	"""

	start = 0
	end = len(listy) - 1
	while start < end:
		middle = end // 2
		if listy[middle] == item:
			return middle
		elif listy[middle] < item:
			start = middle + 1
		else:
			end = middle - 1
	return -1


def scoregen(n):
	"""(int) -> list

	Generates a list of random scores"""
	from random import randint
	from random import choice
	glist = []
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	num = 0
	while n > len(glist):
		glist.append(Score(randint(0,200),
			'{}{}{}'.format(choice(alphabet), choice(alphabet), choice(alphabet))))
	return glist


if __name__ == '__main__':
	import doctest
	doctest.testmod()