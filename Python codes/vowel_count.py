vowels = 'aeiou'

ip_str = 'Hacktoberfest is a platform for beginners to start opensource contribution'

ip_str = ip_str.casefold()

count = {}.fromkeys(vowels,0)

for char in ip_str:
   if char in count:
       count[char] += 1

print(count)
