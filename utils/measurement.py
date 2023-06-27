from timeit import default_timer as timer

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = timer()
        result = func(*args, **kwargs)
        end_time = timer()
        execution_time = int((end_time - start_time) * 1000)
        print(f"Execution time of {func.__name__}: {execution_time} milliseconds")
        return result
    return wrapper
