def myfunc():
    global a
    a=4
    b=6
    result=a+b
    print(result)
    print(f"b is local variable : {b}")


myfunc()
a=a+1
print(f"a is global variable : {a}")


