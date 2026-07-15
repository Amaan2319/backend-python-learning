def outer_Decorator(param):
    def decorator_function(original_function):
        def wrapper_function(*args,**kwargs):
            print(f"Running before {original_function.__name__} with {param}")
            result = original_function(*args,**kwargs)
            print(f"Running after {original_function.__name__} with {param}")
            return result
        return wrapper_function
    return decorator_function

@outer_Decorator("aalu lelo")
def kese_ho(name):
    return f"Acha hu. Tum batao {name}"

print(kese_ho("Amaan"))
# print(kese_ho("Amaan"))