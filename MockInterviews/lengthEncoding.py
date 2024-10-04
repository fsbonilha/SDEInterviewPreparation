def lengthEncoding(text: str) -> str:
	counter = 1
	result = ""
	size = len(text)
	for index in range(size):
		if index < size - 1 and text[index] == text[index + 1]:
			counter += 1
		else:
			result = result + str(counter) + text[index]
			counter = 1
	return result