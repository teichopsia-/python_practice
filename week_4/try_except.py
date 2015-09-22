def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError, e:
        print "division by zero! {}".format(e)
    except TypeError:
        divide(int(x), int(y))
    else:
        print "result is: {}".format(result)
    finally:
        print "executing finally clause"
        
###################################

def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom) for item in list_of_numbers]
   
def SimpleDivide(item, denom):
    try:
        return item / denom
    #catch a division by zero and return 0
    except ZeroDivisionError, e:
        return 0

###################################

def getRatios(v1, v2):
    """
    Assumes: v1 and v2 are lists of equal length of numbers 
    Returns a list containing the meaningful values of v1[i]/v2[i]
    """
    ratios = []
    for index in range(len(v1)):
        try:
            ratios.append(v1[index] / float(v2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('getRatios called with bad arg')
        return ratios
