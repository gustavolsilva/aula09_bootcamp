from functools import wraps
import time
# Decorador de medida de tempo
def time_mensure_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo de execucao da funcao {func.__name__}: {end_time - start_time}")
        return result
    return wrapper