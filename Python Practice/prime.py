
def prime(start, end):
    ls =[]
    flag=0
    for i in range(start,end):
        for j in range(2,i):
            if(i%j==0):
                flag=1
                break

            else:
                flag=0

        if(flag==0):
            ls.append(i)

    return ls


start = 2
end =7

ls = prime(start, end)
if len(ls)==0:
    print("There ais no prime number")

else:
    print("The prime numbers in this are",ls)