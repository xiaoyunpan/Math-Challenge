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
            print("-----------------------------------------")
        else:
            print("错误!|That's wrong!")
            print("正确答案为：|The correct answer is:")
            print(c)
            print("-----------------------------------------")
