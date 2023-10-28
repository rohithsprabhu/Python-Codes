#operator overloading
#+ -> operator
#Magic methods in python if you write  a program which will add two number
#it'll call the method in int __add__()this is a method to add two numbers
a=5
b=8
print(a+b)
print(int.__add__(a,b))
print(int.__invert__(a))
class Student:

    def __init__(self, m1, m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    #define your own funtion to add this is operator overloading
    def __gt__(self, other):
        st1 = self.m1+self.m1
        st2 = other.m1+other.m2
        if st1>st2:
            return True
        else:
            return False
    #override
    def __str__(self):
        #another type return '{} {} '.format(self.m1, self.m2)
        return f'{self.m1} {self.m2} '

s1 = Student(73, 44)
s2 = Student(64, 89)
s3 = s1 + s2#in our code ->Student.__add__(s1,s2)
print(s3.m1)
print(s3.m2)
s4=s1+s2
print(s4.m1)
if s1>s2:
    print('s1 wins')
else:
    print('s2 wins')

a = 2
print(a.__str__())#a.__str__()

print(s1)#s1.__str__() 
