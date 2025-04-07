
def r01():
    content = input("请输入内容：")
    print("您输入的内容是:", content)

def r02():
    f = open("/Users/chason_eil/Desktop/Personal/py1.txt", "r")
    print("----------------")
    print(f.name)
    print(f.mode)
    f.close()

# r02()

def r03():
    f = open("/Users/chason_eil/Desktop/Personal/py1.txt", "r")
    contents = f.read()
    print(contents)
    f.close()

# r03()

def r04():
    f = open("/Users/chason_eil/Desktop/Personal/py1.txt", "r")
    content = f.read(10)
    print(content)
    print("current index:", f.tell())
    print("set pointer to start.")
    f.seek(0, 0)
    print("now index:", f.tell())
    f.close()

# r04()

def r05():
    f = open("/Users/chason_eil/Desktop/Personal/py2.txt", "w+")
    f.write("Write python.\nHello Python.\n")
    f.close()
    print("write done")

# r05()

import os

def r06():
    os.rename("/Users/chason_eil/Desktop/Personal/py1.txt", "/Users/chason_eil/Desktop/Personal/py01.txt")
    print("rename done")

def r07():
    os.remove("/Users/chason_eil/Desktop/Personal/py01.txt")
    print("del file")

def r08():
    os.mkdir("/Users/chason_eil/Desktop/Personal/py01")
    print("create py01")

def r09():
    os.rmdir("/Users/chason_eil/Desktop/Personal/py01")
    print("del py01")

def r10():
    try:
        x = 10/0
        print(x)
    except ZeroDivisionError:
        print("Error: caught exception!")

def r11():
    try:
        f = open("D:/temp/a.txt", "r")
        print(f.name)
    except:
        print("caught error!")

def r12():
    try:
        print("do try")
        x = 1 / 0
    except:
        print("caught exception")
    finally:
        print("do finally")

def r13(num):
    if num < 1:
        raise Exception("Number under 1 exception!")
    else:
        print("current number:", num)

r13(0)
