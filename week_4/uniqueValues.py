def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns a list of keys that map to integer values
    sorted in increasing order
    if empty, return empty list.
    '''
    values = aDict.values()
    b = {}
    final = []
    for k, v in aDict.iteritems():
        b[v] = b.get(v, 0) + 1
    for m, n in b.iteritems():
        if n == 1:
            final.append(m)
    print final
        
    
        

        
uniqueValues({1: 1, 2: 2, 3: 3})  
                [1, 2, 3]   
                
uniqueValues({1: 1, 2: 1, 3: 1})
                    []
                    
uniqueValues({1: 1, 2: 1, 3: 3})
                    [3]
                    

