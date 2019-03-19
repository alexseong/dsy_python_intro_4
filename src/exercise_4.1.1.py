'''
Exercise 1: Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None.
Then write a function called middle that takes a list and returns a new list
that contains all but the first and last elements.
'''

def chop(lst):
    lst.remove(lst[0])
    lst.remove(lst[-1])

def middle(lst):
    return lst[1:-1]

if __name__ == '__main__':
    test_lst1 = [1, 2, 3, 4, 5]
    test_lst2 = [1, 2, 3, 4, 5]

    chop(test_lst1)
    print("test_lst1", test_lst1)

    rtn_lst2 = middle(test_lst2)
    print("test_lst2", test_lst2)
    print("Returned test_lst2", rtn_lst2)
