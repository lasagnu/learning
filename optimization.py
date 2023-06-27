from utils.measurement import measure_execution_time

@measure_execution_time
def suboptimal_add_x_characters_to_string(initial_string: str, x: int):

    """
    This function demonstrates a quirk in Python regarding string concatenation.
    Strings in Python are immutable, meaning they cannot be modified in-place.
    Thus, each time the loop runs to concatenate the character 'a' to the string,
    a new string object is created, resulting in suboptimal performance for large values of `x`.
    """

    for _ in range(x):
        initial_string += 'a'
    return initial_string

@measure_execution_time
def optimal_add_x_characters_to_string(initial_string: str, x: int):

    """
    This function optimizes the process of adding 'a' characters to a string by utilizing
    a more efficient data structure and avoiding the string concatenation quirk in Python.
    """
    characters = [initial_string]
    characters.extend(["a"] * x)
    return ''.join(characters)

if __name__ == '__main__':
    out_string = suboptimal_add_x_characters_to_string(initial_string = "string", x = 10000000)

    out_string2 = optimal_add_x_characters_to_string(initial_string = "string", x = 10000000)