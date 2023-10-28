#idempotence
"""Definition : The property of certain operations in mathematics and 
computer science, that can be applied multiple times without changing 
the result beyond the initial application-via wikipedia"""
#f(f(x))=f(x)if you have a function 'f' and parameters 'x' the result of f(x)
#and you pass the result of f(x) to the same function and it would be
#equal to the value of f(x)
def add_ten(num):
	return num+10
#f(f(x)) = f(x)
print(add_ten(add_ten(10)), add_ten(10))#not idempotent

print(abs(-10), abs(abs(-10)))#idempotent
#abs(-10) == 10
#abs(10) == 10
#abs(10) == 10
a = 10#everytime you run this statement you're gonna get the same value
#POST in http is not idempotent
#GET is idempotent
#DELETE idempotent