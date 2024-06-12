def display(name):
    def message():
        return "Hello "
    result = message()+name
    return result
print(display("Anish"))


'''
Output:

Hello Anish
'''