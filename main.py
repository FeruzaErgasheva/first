a=int(input())
b=int(input())
print(a+b)

def tub(num):
    sum=0
    for i in range(1,num+1):
        sum+=1 if not num%i else 0
    return True if sum==2 else False

func=lambda x:x**2
toq=lambda x:x%2
mylist=list(map(func,range(a,b)))
toq_sonlar=list(filter(toq,range(a,b)))
tub_sonlar=list(filter(tub,range(a,b)))

print(toq_sonlar)
print(mylist)
print(tub_sonlar)