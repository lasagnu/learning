def append_to_list(item, my_list=[]):
    """
    In this function, the default argument my_list is initialized only once, so subsequent function calls modify the same list. 
    """
    my_list.append(item)
    return my_list

def fixed_append_to_list(item, my_list=None):
    """
    To avoid this behavior, it is recommended to use an immutable default argument value or use None as the default value and initialize the mutable object inside the function.
    """
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

if __name__ == '__main__':
    print(append_to_list(1))
    print(append_to_list(2))
    print(append_to_list(3))

    print(fixed_append_to_list(1))
    print(fixed_append_to_list(2))
    print(fixed_append_to_list(3))