import math_tz
print("欢迎使用数学挑战程序！| Welcome to the Math Challenge Program!")
print("-----------------------------------------")
print("乘法挑战请按1,加法挑战请按2，除法挑战请按3，减法挑战请按4,退出请按0。           Press 1 for multiplication challenge, 2 for addition challenge, 3 for division challenge, 4 for subtraction challenge, and 0 for exit.")
print("-----------------------------------------")
a=input("请选择...|Please choose...   ")
a=int(a)
if a==1:
    math_tz.chengfa()
if a==2:
    math_tz.jiafa()
if a==3:
    print("There is a problem with this module, please do not use it.")
if a==4:
    math_tz.jianfa()
if a==0:
    exit()
