def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1

arr = [10, 20, 30, 40, 50]
element = 20
result = search(arr, element)
if result == -1:
    print(element," not exist")
else:
    print(element, " exist at index ", result)