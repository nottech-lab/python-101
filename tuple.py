'''
Write a simple script to demonstrate your understanding of tuples as data types
'''

# first example

def quotient_ramainder(x, y):
    q = x // y
    r = x % y

    return (q, r)

(quotient, remainder) = quotient_ramainder(9, 7)

print('The quotient is', quotient)
print('The remainder is', remainder)

# second example

def process_data(aTuple):
    nums = ()
    words = ()

    for t in aTuple:
        nums = nums + (t[0],)

        if t[1] not in words:
            words = words + (t[1],)

    min_number = min(nums)
    max_number = max(nums)
    words_size = len(words)

    return (min_number, max_number, words_size)


aTuple = ((2014, 'Fast and Furious'),
          (2015, 'Fast and Furious'),
          (2017, 'Captain America'),
          (2018, 'Black Panther'),
          (2019, 'Avengers'))

(min_year, max_year, words_length) = process_data(aTuple)

print('From', min_year, 'to', max_year, 'i had watched', words_length, 'favorite movies')
