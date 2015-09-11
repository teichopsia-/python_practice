# List practice

# l = [expression, ....]
l = []
l2 = [1, 2, 3, 4, 5]
l3 = ["one", "two", "three"]

# list comprehension

# l = [expression for variable in sequence]
# The sequence can be any kind of sequence object or iterable,
# including tuples and generators. 
l4 = [numbers
    for numbers in range(5)]
    
l5 = [more
    for more in range(5)
    if more % 2 == 0]
    
l6 = list()
l7 = list(range(5))
l8 = list(number for number in range(5))

# will point to the same list
l9 = l10 = []
l11 = []
l12 = l11

# prints both the index and item, using enumerate

for index, item in enumarate(l):
    print index, item
    
# if you only need the index
for index in range(len(l)):
    print index
    
# lists objects support the iterator protocol. To create an iterator,
# use iter
i = iter(l)
item = i.next() #fetches the first value
item = i.next() #fetches the second value, and so on....

sum(l) # sums the items in a list if they are numbers

# you can joing single long strings using join

some_list = ["hello", "how", "are", "you", "?"]
s = ''.join(some_list)

# the del statement can be used to remove an item
del l[3]    #single item
del l[2:5]  #multiple items

item = l3.pop() #last item
item = l3.pop(3) #at given index
item = l3.pop(index)
l.remove(item) #searches for an item, removing the first ocurrence.

# pop returns the item removed while del doesn't.
