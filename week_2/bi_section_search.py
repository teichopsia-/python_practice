x = 3
ans = 0
itersLeft = x

while itersLeft != 0:
    ans += x
    itersLeft -= 1
    print(str(x) + '*' + str(x) + '=' + str(ans))
    
    
x = int(raw_input("Enter an integer: "))

for ans in range(0, abs(x) + 1):
    if ans ** 3 == abs(x):
        break
if ans ** 3 != abs(x):
    print(str(x) + 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))
