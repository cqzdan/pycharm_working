for i in range(4):
    if i==0 or i ==3:
        print ("* "*5)
    else:
        for n in range(5):
            if n==0 | n==4:
                print ('*       *')



#字符串中非关键字参数应用
string = ("你的名字是{name}，你今年{year}了")
rem = string.format(name="淡移波",year="38岁")
print(rem)

