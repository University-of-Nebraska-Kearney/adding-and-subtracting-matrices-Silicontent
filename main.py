def main() -> None:
	# used for function testing
	print("MATRIX 1 ===")
	m1 = get_matrix()
	print("\nMATRIX 2 ===")
	m2 = get_matrix()
	print("\nADDING MATRICES ===")
	print(add_matrix(m1, m2))


def get_matrix() -> list[list]:
	"""
	Function that creates a matrix of elements based on user input. The user
	specifies the dimensions of the matrix before specifying the individual
	elements.

	:return: a 2D list representing the generated matrix
	"""

	# get number of rows and columns
	row: int = get_natural_number("How many rows?  ", False)
	col: int = get_natural_number("How many columns?  ", False)
	print()

	matrix: list[list] = []

	# get data for each element in the matrix from the user
	for r in range(row):
		# add new row to the matrix
		matrix.append([])
		for c in range(col):
			elem = get_float(f"Enter a number for element [{r + 1}, {c + 1}]: ")
			# add element to the row
			matrix[r].append(elem)

	return matrix


def get_natural_number(prompt: str = "Enter a positive number: ", negative: bool = True) -> int:
	"""
	Function that gets a whole number from the user, validates it, and returns it.
	This function does not allow the input of decimal numbers.

	:param prompt: string displayed to instruct the user on what to enter
	:param negative: boolean that, if true, allows numbers less than or equal to 0
	:return: whole number gotten from the user
	"""

	num: int = 0
	valid: bool = False

	# get a whole number from the user
	while not valid:
		try:
			num = int(input(prompt))
			# if negatives not allowed, ensure number is above zero
			if not negative and num <= 0:
				print("Please enter a number greater than 0.")
			else:
				valid = True
		except ValueError:
			print("Please enter a whole number.")

	return num


def get_float(prompt: str = "Enter a number: ") -> float:
	"""
	Function that gets a floating point number from the user, validates it,
	and returns it.

	:param prompt: string displayed to instruct the user on what to enter
	:return: float representing a number gotten from the user
	"""

	num: float = 0.0
	valid: bool = False

	while not valid:
		try:
			num = float(input(prompt))
			valid = True
		except ValueError:
			print("Please enter a number.")

	return num


def add_matrix(m1: list[list], m2: list[list]) -> list[list]:
	"""
	Function that takes two matrices and adds them together by adding
	corresponding elements from each matrix. Matrices of non-matching
	sizes cannot be added.

	:param m1: one matrix to be added
	:param m2: the other matrix to be added
	:return: a 2D list representing a matrix of m1 + m2, or an empty
	list if the two matrices cannot be added
	"""

	sum: list[list] = []

	# verify that the two matrices can be added together
	if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
		# walk through the matrix and add corresponding elements
		for r in range(len(m1)):
			sum.append([])
			for c in range(len(m1[0])):
				sum[r].append(m1[r][c] + m2[r][c])
	else:
		print("Given matrices cannot be added together.")

	return sum


if __name__ == "__main__":
	main()
