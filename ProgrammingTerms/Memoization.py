#Memoization
#Definition - Memoization is an optimization technique used primarily to speed up (Dynamic Programming) 
#computer programs by storing the results of expensive function calls and returning
#the coached result when the same inputs occur again
import time

ef_cache = {}

def expensive_func(num):
	if num in ef_cache:
		return ef_cache[num]
	print("Computing {} ...".format(num))
	time.sleep(1)
	result = num * num
	ef_cache[num] = result
	return result

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)
#instead of computing for the same input again store the result of input and if it comes again as an input then display the same result again is known as memoization
#saving the result in cache