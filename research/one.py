# # # # Decorator function
# # # def logger(func):
# # #     def wrapper(*args, **kwargs):
# # #         print(f"Function '{func.__name__}' called with args: {args}, kwargs: {kwargs}")
# # #         result = func(*args, **kwargs)
# # #         print(f"Function '{func.__name__}' returned: {result}\n")
# # #         return result
# # #     return wrapper

# # # def logger2(func):
# # #     def wrapper(*args, **kwargs):
# # #         print("log21")
# # #         result = func(*args, **kwargs)
# # #         print("log22")
# # #         return result
# # #     return wrapper


# # # # Add function
# # # @logger
# # # def add(a, b):
# # #     return a + b

# # # # Subtract function
# # # # @logger
# # # def sub(a, b):
# # #     return a - b

# # # # Example usage
# # # x = 10
# # # y = 5

# # # # add(x, y)
# # # # sub(x, y)

# # # @logger2
# # # @logger

# # # def lmn():
# # #     print("lmn function")


# # # lmn()












# a=10
# b=20

# # def abc(a, b):
# #     a = a + b
# #     b = b + b
# #     print(a)
# #     print(b)


# # abc(a,b)
# # print(a)
# # print(b)

# c=10
# d=20

# def edc(*args):
#     a = c+d
#     b = d+d
#     print(a)
#     print(b)

# edc(c,d)

c=1
d=4
values = [10, 20]
def edc(**args):
    c = 100
    d = 200
   
    print(c)
    print(d)

edc(values)

print(c)
print(d)
