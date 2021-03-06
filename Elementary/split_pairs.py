#!/usr/bin/env checkio --domain=py run split-pairs

# Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').
# 
# Input:A string.
# 
# Output:An iterable of strings.
# 
# Precondition:0<=len(str)<=100
# 
# 
# END_DESC

def split_pairs(a):
    even = a[::2]
    odd = a[1::2] + '_'
    tuples = list(zip(even, odd))
    result = [x[0] + x[1] for x in tuples]
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")