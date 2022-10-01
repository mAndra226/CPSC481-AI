# check if specified row and column are valid matrix index
def isValid(i, j, N, M):
	return (0 <= i < M) and (0 <= j < N)


# Replace all O's in a matrix with their shortest distance
# from the nearest trap
def shortestDistanceToTraps(mat):
	# start writing from here
	


if __name__ == '__main__':

	mat = [
		['O', 'O', 'T', 'O', 'O'],
		['O', 'W', 'O', 'T', 'O'],
		['W', 'T', 'O', 'O', 'W'],
		['O', 'O', 'O', 'O', 'O']
	]

	result = shortestDistanceToTraps(mat)

	# print results
	for r in result:
		print(r)
