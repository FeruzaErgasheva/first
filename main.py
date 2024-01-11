a=int(input())
b=int(input())
print(a+b)

func=lambda x:x**2
toq=lambda x:x%2
mylist=list(map(func,range(a,b)))
toq_sonlar=list(filter(toq,range(a,b)))
print(toq_sonlar)
print(mylist)