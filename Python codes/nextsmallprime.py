def nsmallestprime(n :int)-> int :
  if n < 2 :
    raise ValueError("n must be greater than 2")
  def prime(i):
    return all(i % j != 0 for j in range(2, int(i ** 0.5 + 1)))
  for i in range ( n , 1 , -1):
    if prime(i):
      return int(i)
if __name__ == "__main__":
  print(nsmallestprime(100001))
# prints 99991 
  
