def FancyDivide(numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
    except Exception, e:
        print e
        
        
def FancyDivide2(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception, e:
        print e
        
def FancyDivide3(numbers, index):
    denom  = numbers[index]
    return [SimpleDivide(item, denom)
            for item in numbers]
            
def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0
        
def Normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "Output not between 0 and 1"
    return numbers
