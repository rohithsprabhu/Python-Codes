num = 1634

order = len(str(num))

result = 0

temp = num
while temp > 0:
   digit = temp % 10
   result += digit ** order
   temp //= 10

if num == result:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
