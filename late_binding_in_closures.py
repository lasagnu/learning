def faulty_function():
    """
    In the above example, even though numbers is modified after the inner function is defined, the closure still references the updated value of numbers when it is called. 
    This is due to late binding, where variable lookup happens at runtime.
    """
    numbers = [1, 2, 3]

    def faulty_inner_function():
        return [num * 2 for num in numbers]

    numbers = [4, 5, 6]  # Modifying the outer variable

    return faulty_inner_function()

def proper_function():
    numbers = [1, 2, 3]

    def proper_inner_function(numbers=numbers):
        return [num * 2 for num in numbers]

    numbers = [4, 5, 6]  # Modifying the outer variable

    return proper_inner_function()

if __name__ == '__main__':
    print(faulty_function())
    print(proper_function())