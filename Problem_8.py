# 7.Write a program find the sum of all the even numbers of the list.
a=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in a:
    if(i%2==0):
        sum+= i
print(sum)        