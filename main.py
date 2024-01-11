a=int(input())
b=int(input())
print(a+b)

func=lambda x:x**2
mylist=list(map(func,range(a,b)))
print(mylist)