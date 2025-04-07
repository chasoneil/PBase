# pytho exception

# 1. try-except block for specific exception
def demo1():
    try:
        x = 10/0
        print(x)
    except ZeroDivisionError:
        print("Error: division by zero")

# demo1()

# 2. catch all exception
def demo2():
    try:
        a = 10 / 0
        print(a)
    except:  # do not recommend
        print("Error: your code caught exception")

# demo2()

# 3. try except finally
def demo3():
    try:
        x = 10 / 0
        print(x)
    except ZeroDivisionError:
        print("Error: division by zero")
    finally:
        print("finally coding")

# demo3()

# 4. try-except-else
def demo4():
    try:
        print("do try")
    except:
        print("caught except.")
    else:
        print("no except.")

# demo4()

# 5. throw exception
def demo5(level):
    if level < 1:
        raise Exception("level is under 1!")
    print("level:", level)

demo5(0)


