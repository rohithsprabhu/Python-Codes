#most important
#scope-> var can be acceessed from within the program and what values those variables hold in different contexts
#LEGB -(stands for) local, enclosing, global and built-in->order of checking 
#x = 'global x' even if you cmt this line it won't affect the program if you declare a global x inside the fiunction
import builtins

print(dir(builtins))
#Note: if you declare a function in the same name of builtin function.Python takes your function first if you pass
#any argument wrongly you'll get error(ex: def min():pass)

def test(z):
	#global x #global scope if you cmt this line and if you try to print the var(inside the func) outside the func it'll raise error
	x = 'local x'
	#print(y)
	print(x)
	print(z)
test('local z')#even you pass the value in parameter it becomes local to the specific function
#print(y)#error it is local var to the test function
#print(x)
#print(z) error
#builtin function
m = min([3,4,6,6,7,78,5,4])
print(m)
x = 'global x'
def outer():
	x = 'outer x'#if we cmt this it'll raise error
	def inner():
		nonlocal x#now its affect the x var in outer x without affecting the global x var
		x = 'inner x'
		#x = 'inner x'#local scope of inner function if you cmt this line enclosing scope
		#if first check local to the inner function and it doesn't(we commented it)
		#and it checks any var in the local scope of any enclosing function(outer function)
		#encloosing enclosure function is outer function
		print(x)
	inner()
	print(x)
outer()
print(x)