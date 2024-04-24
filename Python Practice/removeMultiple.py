#
# list1 = [11, 5, 17, 18, 23, 50]
#
# for ele in list1:
# 	if ele % 2 == 0:
# 		list1.remove(ele)
#
# print("New list after removing all even numbers: ", list1)


list1=[]

n=int(input("Enter no. of ele"))

for i in range(1,n+1):
    nums = int(input("Enter element: "))
    list1.append(nums)

for ele in list1:
    if ele % 2==0:
        list1.remove(ele)

print("New list is: ",list1)