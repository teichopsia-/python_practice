# How to test code

def average(num_list):
    """ 
    calculate the average of numbers in a list
    """
    assert len(num_list) >= 1, 'List must be greater than 0'
    n = len(num_list)
    count = 0
    for a in num_list:
        count += a
    total = count / n
    return total


def running(values):
    assert len(values) > 0
    assert result[-1] >= 0
    result.append(result[-1] + v)
    assert result[-1] > = result[0] 
    return result
    
    
