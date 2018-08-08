#这是打印乘法表的函数
def multiplication_table(number):
    '''
    #以下描述函数中定义的变量和返回值
    :param number: 传入值必须为Int类型
    这个数为用户传入本函数的打印数字，函数将以该数字作为闭合区间打印该数字以内所有的乘法表
    :return: 该函数没有返回值
    '''
    for row in range(1,number+1):
        for col in range(1,row+1):
            print("{0}*{1}={2}".format(row,col,row*col)," ",end="")
        print()

print ("# " * 30)
multiplication_table(7)
print("$ " * 30)
help(multiplication_table)
print("& " * 30)
print(multiplication_table.__doc__)


s1 = "i love zdan"
s2 = s1.__len__()
print(s2)
