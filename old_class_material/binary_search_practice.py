a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

num = ???           |
L = [2, 0, 1, 5, 3, 4]
val = 0
for i in range(0, num):
    val = L[L[val]]

print val
        

def rBinarySearch(list_elements, element):
    if len(list_elements) == 1:
        return element == list_elements[0]
    mid = len(list_elements) / 2
    if list_elements[mid] > element:
        return rBinarySearch(list_elements[ : mid], element)
    if list_elements[mid] < element:
        return rBinarySearch(list_elements[mid : ], element)
    return True

