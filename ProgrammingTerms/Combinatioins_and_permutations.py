#combinatioins and permutations
#combinations - a combination is all the different ways in which you can group something
#where the order doesnot matter
#permutations - all the different ways in which you can group some values in which the order does matter
import itertools

my_list = [1,2,3,4,5,6]
"""
combinations = itertools.combinations(my_list, 2)
for c in combinations:
	print(c)

print("permutations")
permutations  =itertools.permutations(my_list, 2)
for p in permutations:
	print(p)"""
combinations = itertools.combinations(my_list, 3)
permutations = itertools.permutations(my_list, 3)
print([result for result in combinations if sum(result) == 10])#combinations wins its appropriate for this problem
print([result for result in permutations if sum(result) == 10])

word = 'sample'
my_letters = 'plmeas'

combinations  = itertools.combinations(my_letters, 6)
permutations = itertools.permutations(my_letters, 6)

for p in permutations:#permutations wins every each other combination of letter or number
	print(p)
	if ''.join(p) == word:
		print("match!")
		break
else:
	print("No match")

for c in combinations:
	print(c)
	if ''.join(c) == word:
		print("match!")
		break
else:
	print("No match")
