def scope_test():
    x = 22

#print(f"This is the variable value: {x}")
#NameError: name 'x' is not defined

def scope_test():
    x = 22
    return x

y = scope_test()
print(y)
