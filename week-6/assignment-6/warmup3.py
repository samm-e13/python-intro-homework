def scope_test():
    x = 22
    return x

#print(f"This is the variable value: {x}")
#NameError: name 'x' is not defined

y = scope_test()
print(y)
