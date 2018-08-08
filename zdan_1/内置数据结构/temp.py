import copy
a = [["one", 1, "eins"], ["two", 2], ["three", 3,4,5,6,8] ]
'''
print(id(a[1]))
#b = copy.deepcopy(a)
b = a.copy()
print(id(b[1]))



print(id(a))
b = a.copy()
print(b)
print(id(b))

help()

# 多循环的集合内涵
s1 = {1,2,3,4}
s2 = {"i", "love", "wangxiaojing"}


s = {m*n for m in s2 for n in s1 if n ==2}
print(s)

b1 = {i for i in range(1,100) if i % 2 == 0}
print(b1)
print(id(b1))
b2 = b1.pop()
print(b2)
print(id(b2))
if 2 in b1:
    print("yes")
else:
    print("no")
'''

dict1 = {'a':1, 'b':2, 'c':3}
for k,v in dict1.items():
    print(k ,"--", v)
    print(k,"--",type(k))
print()
dict2 = dict1.fromkeys('b',5)
print(type(dict2))
print(dict2)