def search(L, element):
    for i in range(len(L)):
        if L[i] == element:
            return True
    return False

def search2(L, element):
    for i in range(len(L)):
        if L[i] == element:
            return True
        if L[i] > element:
            return False
    return False


num = ???
L = [5, 0, 2, 4, 6, 3, 1]
L = [2, 0, 1, 5, 3, 4]
val = 0
for i in range(0, num):
    val = L[L[val]]

print val
