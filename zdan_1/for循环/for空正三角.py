n=int(input("输入需打印空心三角的行数："))
a = "* "
b = " "
t = n
for i in range(n):
    #起始位置打印空格
    for j in range(t-1,0,-1):
        print(b, end="")
    for k in range(n-i-1,n):
        #判断第一行和最后一行打印*
        if i==n-1 or k==n-i-1 or k==n-1:
            print(a, end="")
        else:
            print(b * 2, end="")
    print()
    t -= 1

