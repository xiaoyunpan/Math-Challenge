import random
def chengfa():
    while True:
        a=random.randint(1,20)
        b=random.randint(1,20)
        c=a*b
        print(a)
        print("×")
        print(b)
        d=input("等于几: | Equal to a few: ")
        d=int(d)
        if d==c:
            print("正确!|You are right!")
            print("如果你想退出，请按0键。| If you want to exit, press the 0 key.")
            print("-----------------------------------------")
        if d==0:
            exit()
        else:
            print("错误!|That's wrong!")
            print("正确答案为：|The correct answer is:")
            print(c)
            print("如果你想退出，请按0键。| If you want to exit, press the 0 key.")
            print("-----------------------------------------")
def jiafa():
    while True:
        a=random.randint(1,100)
        b=random.randint(1,100)
        c=a+b
        print(a)
        print("+")
        print(b)
        d=input("等于几: | Equal to a few: ")
        d=int(d)
        if d==c:
            print("正确!|You are right!")
            print("如果你想退出，请按0键。| If you want to exit, press the 0 key.")
            print("-----------------------------------------")
        if d==0:
            exit()
        else:
            print("错误!|That's wrong!")
            print("正确答案为：|The correct answer is:")
            print(c)
            print("如果你想退出，请按0键。| If you want to exit, press the 0 key.")
            print("-----------------------------------------")
def chufa():
    while True:
        a=random.randint(1,10)
        b=random.randint(1,10)
        c=a/b
        print(a)
        print("÷")
        print(b)
        d=input("等于几: | Equal to a few: ")
        d=int(d)
        if d==c:
            print("正确!|You are right!")
            print("如果你想退出，请按0键。| If you want to exit, press the 0 key.")
            print("-----------------------------------------")
        if d==0:
            exit()
        else:
            print("错误!|That's wrong!")
            print("正确答案为：|The correct answer is:")
            print(c)
            print("如果你想退出，请按0键。| If you want to exit, press the 0 key.")
            print("-----------------------------------------")
def jianfa():
    while True:
        a=random.randint(1,20)
        b=random.randint(1,20)
        c=a-b
        print(a)
        print("-")
        print(b)
        d=input("等于几: | Equal to a few: ")
        d=int(d)
        if d==c:
            print("正确!|You are right!")
            print("如果你想退出，请按0键。| If you want to exit, press the 0 key.")
            print("-----------------------------------------")
        if d==0:
            exit()
        else:
            print("错误!|That's wrong!")
            print("正确答案为：|The correct answer is:")
            print(c)
            print("如果你想退出，请按0键。| If you want to exit, press the 0 key.")
            print("-----------------------------------------")
