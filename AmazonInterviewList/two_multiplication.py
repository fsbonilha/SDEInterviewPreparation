# Given an array of integers A and an integer number X, find all pairs of indices (i, j), i < j, such that A[i] * A[j] == X.

# A = [6, 3, 2, 4, 5, 10]

# Target = 20

# Questions: É garantido que não terei valores repitidos? Se tiver valores repetidos, devo contar os dois?


from typing import List


def two_multiplication(nums: List[int], target: int) -> List[List[int]]:
	visited = {}
	result = []

	for idx, num in enumerate(nums):
		pair = target / num
		if pair in visited:
			result.append([visited[pair], idx])
		visited[num] = idx
	return result

print(two_multiplication([6, 3, 2, 4, 5, 10], 20))

print(two_multiplication([1,2,3,4,5,6,7,8,9,10,11,12,24], 24))
