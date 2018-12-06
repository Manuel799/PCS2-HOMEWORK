import timeit
setup="""
def mergesort( lst ) :
    if len ( lst ) == 1 :
        return lst
    left = lst [ 0 : len( lst ) // 2 ]
    right = lst [ len( lst ) // 2 : ]
    left = mergesort( left )
    right = mergesort( right )
    return merge( left , right )

def merge( left , right ) :
    result = []
    while len( left ) > 0 and len( right ) > 0 :
        if left[ 0 ] <= right[ 0 ] :
            result.append( left.pop( 0 ) )
        else :
            result.append( right.pop( 0 ) )
    while len( left ) > 0 :
         result.append( left.pop( 0 ) )
    while len( right ) > 0 :
          result.append( right.pop( 0 ) )
    return result



def quickSort(lst):
    if len(lst) > 1:
        piv = lst[0]
        left = []
        right =[]
        for i in range(1, len(lst)):
            if (lst[i] < piv):
                left.append(lst[i])

            else:
                right.append(lst[i])
        return quickSort(left) + [piv] + quickSort(right)

    else:
        return lst

import random
my_randoms0 = random.sample(range(50), 10)
my_randoms1 = random.sample(range(500), 100)
my_randoms2 = random.sample(range(5000), 1000)
my_randoms3 = random.sample(range(50000), 10000)
"""
t0=timeit.Timer('quickSort(my_randoms0)',setup = setup)
t1=timeit.Timer('quickSort(my_randoms1)',setup = setup)
t2=timeit.Timer('quickSort(my_randoms2)',setup = setup)
t3=timeit.Timer('quickSort(my_randoms3)',setup = setup)
t4=timeit.Timer('mergesort(my_randoms0)',setup = setup)
t5=timeit.Timer('mergesort(my_randoms1)',setup = setup)
t6=timeit.Timer('mergesort(my_randoms2)',setup = setup)
t7=timeit.Timer('mergesort(my_randoms3)',setup = setup)
print('quicksort time:',t0.timeit(5))
print('mergesort time:',t4.timeit(5))
print('quicksort time:',t1.timeit(5))
print('mergesort time:',t2.timeit(5))
print('quicksort time:',t3.timeit(5))
print('mergesort time:',t5.timeit(5))
print('quicksort time:',t6.timeit(5))
print('mergesort time:',t7.timeit(5))
