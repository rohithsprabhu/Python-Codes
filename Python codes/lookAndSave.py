a = '1'
n = 4
temp = ''
counter = 1
j = 0
for i in range(n):
    print(a)
    while j < len(a):
        try:
            while a[j] == a[j+1]:
                counter += 1
                j += 1
        except Exception:
            pass
        temp = temp + str(counter) + a[j] 
        counter = 1
        j += 1
    a = temp
    counter = 1
    temp = ''
    j = 0