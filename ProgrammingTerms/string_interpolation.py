#programming terms
#string interpolation
"""definition : The process of evaluating a string literal containing one 
or more placeholders, yielding a result in which the placeholders are 
replaced with their corressponding values-via wikipedia"""
name = 'James Gunn'
age = 28#string concatenation
#greeting = 'My name is ' + name + ' and I am ' + str(age) + ' years old'
#greeting = 'My name is {} and I am {} years old'.format(name, age)#string formatting
#string interpolation
greeting = 'I am {age} years old and My name is {name} '.format(name=name, age=age)
print(greeting)
#placeholders ins string using format method by giving the placeholder a name and use whanever you want to put a values
#string concatenating may be you leave a space that are sometimes messed up with largest string literal
