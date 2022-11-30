def another_function(func):
    """
    A function that accepts another function
    """

    def other_func():
        val = f"The result of {func()} is {eval(func())}"
        # val = 5
        return val
    return other_func

@another_function
def a_function():
    """A pretty useless function"""
    print('ok')
    return "1+1"

if __name__ == "__main__":
    value = a_function()
    print(value)