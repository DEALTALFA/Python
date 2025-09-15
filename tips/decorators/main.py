def decorator(func):
    def wrapper(*args,**kwargs):
        """
        A wrapper function that prints messages before and after calling the decorated function.

        Args:
            *args: Variable length argument list for the decorated function.
            **kwargs: Arbitrary keyword arguments for the decorated function.

        Returns:
            The result of the decorated function.
        """
        print("Before calling the function.")
        func(*args,**kwargs)
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function
def greet(p):
    print("Hello, World!",p)

if __name__ == "__main__":
    greet("nicks")